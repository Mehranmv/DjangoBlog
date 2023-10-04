from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
# local
from django.views import View
from .forms import UserLoginForm, UserRegisterForm, CouponForm
from posts.models import Post
from .models import Membership, Coupon
# third party
import requests
import json
import datetime
from dateutil.relativedelta import relativedelta

######################################## ZARINPAL ###############################################
if settings.SANDBOX:
    sandbox = 'sandbox'
else:
    sandbox = 'www'
ZP_API_REQUEST = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentRequest.json"
ZP_API_VERIFY = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentVerification.json"
ZP_API_STARTPAY = f"https://{sandbox}.zarinpal.com/pg/StartPay/"
amount = 10000
amount2 = 20000
description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"
CallbackURL = 'http://127.0.0.1:8000/accounts/membership/payment-callback/'


######################################## ZARINPAL ###############################################


class UserLoginView(View):
    form_class = UserLoginForm

    def get(self, request):
        form = self.form_class()
        return render(request, 'accounts/login.html', {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, _("خوش آمدید"), 'success')
                return redirect('home:home_page')
            messages.error(request, _("نام کاربری یا کلمه عبور اشتباه است"), 'danger')
            return redirect('accounts:user_login')


class UserLogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.success(request, _("با موفقیت خارج شدید"), 'success')
        return redirect('home:home_page')


class UserRegisterView(View):
    form_class = UserRegisterForm

    def get(self, request):
        form = self.form_class()
        return render(request, 'accounts/register.html', {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(
                username=cd['username'],
                password=cd['password'],
                email=cd['email'],
                first_name=cd['firstname'],
                last_name=cd['lastname']
            )
            messages.success(request, _("حساب کاربری شما با موفقیت ایجاد شد !"), 'success')
            return redirect('accounts:user_login')


class UserProfileView(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        bookmarked_posts = Post.objects.filter(bookmark__user=user)
        membership = Membership.objects.filter(user=request.user)
        context = {
            'user': user,
            'bookmarked_posts': bookmarked_posts,
            'membership': membership
        }
        return render(request, 'accounts/profile.html', context)


class BookmarkView(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        bookmarked_posts = Post.objects.filter(bookmark__user=user)
        context = {
            'user': user,
            'bookmarked_posts': bookmarked_posts
        }
        return render(request, 'accounts/bookmarked_posts.html', context)


class VipView(LoginRequiredMixin, View):
    def get(self, request):
        global amount
        amount = 10000
        amount2 = 20000
        x2 = amount2
        context = {
            'coupon': CouponForm,
            'amount': amount,
            'amount2': x2

        }
        return render(request, 'accounts/buy_membership.html', context)

    def post(self, request):
        global amount, amount2
        amount = 10000
        amount2 = 20000
        form = CouponForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            amounts = Coupon.discount(code=code)
            x = amounts[0]
            x2 = amounts[1]
            context = {
                'coupon': CouponForm,
                'amount': x,
                'amount2': x2
            }
            amount = x
            amount2 = x2
            return render(request, 'accounts/buy_membership.html', context)


class BuyMembershipView(View):
    def get(self, request, id1):
        membership = Membership.objects.filter(user=request.user)
        if not membership:
            global amount, amount2
            x = amount
            if id1 == 1:
                x = amount
            elif id1 == 2:
                x = amount2
            data = {
                "MerchantID": settings.MERCHANT,
                "Amount": x,
                "Description": description,
                "CallbackURL": CallbackURL,
            }
            data = json.dumps(data)
            headers = {'content-type': 'application/json', 'content-length': str(len(data))}
            response = requests.post(url=ZP_API_REQUEST, data=data, headers=headers)
            if response.status_code == 200:
                response = response.json()
                if response['Status'] == 100:
                    url = f"{ZP_API_STARTPAY}{response['Authority']}"
                    return redirect(url)

            else:
                print(response.json()['errors'])
                return HttpResponse(str(response.json()['errors']))
        else:
            messages.error(request, _("شما از قبل اکانت ویژه دارید"), 'danger')
            return redirect('accounts:vip')


class PaymentCallbackView(View):
    def get(self, request):
        authority = request.GET['Authority']
        data = {
            "MerchantID": settings.MERCHANT,
            "Amount": amount,
            "Authority": authority
        }
        data = json.dumps(
            data
        )
        headers = {'content-type': 'application/json', 'content-length': str(len(data))}
        response = requests.post(ZP_API_VERIFY, data=data, headers=headers)

        if response.status_code == 200:
            res = response.json()
            if res['Status'] == 100:
                return render(request, 'accounts/buy_membership_ok.html')
                pass
            else:
                if amount <= 10000:
                    plan = _("طلایی")
                else:
                    plan = _("الماسی")
                Membership.objects.create(user=request.user, start_date=datetime.date.today(),
                                          end_date=datetime.date.today() + relativedelta(months=1), plan_type=plan)
                return render(request, 'accounts/buy_membership_ok.html')
        return render(request, 'accounts/buy_membership_nok.html')


class HistoryView(LoginRequiredMixin, View):
    def get(self, request):
        membership = Membership.objects.filter(user=request.user)
        if membership:
            if membership.last().end_date < datetime.date.today():
                membership.delete()
            return render(request, 'accounts/history.html', {'membership': membership})
        else:
            messages.error(request, 'شما اکانت ویژه نداربد', 'danger')
            return redirect('accounts:user_profile')
