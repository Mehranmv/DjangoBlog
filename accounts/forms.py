from django import forms
from django.utils.translation import gettext_lazy as _


class UserLoginForm(forms.Form):
    username = forms.CharField(
        label=_("نام کاربری"),
        widget=forms.TextInput(
            attrs={
                'class': "form-control"
            }
        )
    )
    password = forms.CharField(
        label=_("کلمه عبور"),
        widget=forms.PasswordInput(
            attrs=
            {
                'class': "form-control"
            }
        )
    )


class UserRegisterForm(forms.Form):
    username = forms.CharField(
        label=_("نام کاربری"),
        widget=forms.TextInput(
            attrs={
                'class': "form-control"
            }
        )
    )
    password = forms.CharField(
        label=_("کلمه عبور"),
        widget=forms.PasswordInput(
            attrs=
            {
                'class': "form-control"
            }
        )
    )
    email = forms.CharField(
        label=_("ایمیل"),
        widget=forms.EmailInput(
            attrs=
            {
                'class': "form-control"
            }
        )
    )
    firstname = forms.CharField(
        label=_("نام"),
        widget=forms.TextInput(
            attrs=
            {
                'class': "form-control"
            }
        )
    )
    lastname = forms.CharField(
        label=_("نام خانوادگی"),
        widget=forms.TextInput(
            attrs=
            {
                'class': "form-control"
            }
        )
    )


class CouponForm(forms.Form):
    code = forms.CharField(label=_("کد تخفیف دارید ؟ وارد کنید"),
                           widget=forms.TextInput(attrs={'class': 'form form-control'}))
