# django imports
from django.shortcuts import render
from django.views import View
# local imports
from .models import AboutUs, ContactUs, Rules, Questions


class AboutUsView(View):
    def get(self, request):
        page = AboutUs.objects.get(slug='aboutus')
        return render(request, 'pages/pages.html', {'page': page})


class ContactUsView(View):
    def get(self, request):
        page = ContactUs.objects.get(slug='contactus')
        return render(request, 'pages/pages.html', {'page': page})


class RulesView(View):
    def get(self, request):
        page = Rules.objects.get(slug='rules')
        return render(request, 'pages/pages.html', {'page': page})


class QuestionsView(View):
    def get(self, request):
        page = Questions.objects.get(slug='questions')
        return render(request, 'pages/pages.html', {'page': page})
