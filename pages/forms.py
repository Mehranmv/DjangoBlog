from django import forms
from django.contrib import admin
from .models import AboutUs, ContactUs, Rules, Questions


class AboutUsForm(admin.ModelAdmin):
    def has_add_permission(self, request):
        if AboutUs.objects.count() == 0:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if AboutUs.objects.count() == 1:
            return True
        return False


class ContactUsForm(admin.ModelAdmin):
    def has_add_permission(self, request):
        if ContactUs.objects.count() == 0:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if ContactUs.objects.count() == 1:
            return True
        return False


class RulesForm(admin.ModelAdmin):
    def has_add_permission(self, request):
        if Rules.objects.count() == 0:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if Rules.objects.count() == 1:
            return True
        return False


class QuestionsForm(admin.ModelAdmin):
    def has_add_permission(self, request):
        if Questions.objects.count() == 0:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if Questions.objects.count() == 1:
            return True
        return False
