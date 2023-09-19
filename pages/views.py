# django imports
from django.shortcuts import render
from django.views import View
# local imports
from .models import AboutUs, ContactUs, Rules, Questions


class AboutUsView(View):
    def get(self, request, page_slug):
        page = AboutUs.objects.get(slug=page_slug)
        return render(request, 'pages/pages.html', {'page': page})


class ContactUsView(View):
    def get(self, request, page_slug):
        page = ContactUs.objects.get(slug=page_slug)
        return render(request, 'pages/pages.html', {'page': page})


class RulesView(View):
    def get(self, request, page_slug):
        page = Rules.objects.get(slug=page_slug)
        return render(request, 'pages/pages.html', {'page': page})


class QuestionsView(View):
    def get(self, request, page_slug):
        page = Questions.objects.get(slug=page_slug)
        return render(request, 'pages/pages.html', {'page': page})
