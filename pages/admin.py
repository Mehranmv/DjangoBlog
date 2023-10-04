from django.contrib import admin
from .models import AboutUs, ContactUs, Rules, Questions


@admin.register(AboutUs)
class AboutUsForm(admin.ModelAdmin):
    list_per_page = 10000000

    def has_add_permission(self, request):
        if AboutUs.objects.count() == 0:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if AboutUs.objects.count() == 1:
            return True
        return False


@admin.register(ContactUs)
class ContactUsForm(admin.ModelAdmin):
    list_per_page = 10000000

    def has_add_permission(self, request):
        if ContactUs.objects.count() == 0:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if ContactUs.objects.count() == 1:
            return True
        return False


@admin.register(Rules)
class RulesForm(admin.ModelAdmin):
    list_per_page = 10000000

    def has_add_permission(self, request):
        if Rules.objects.count() == 0:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if Rules.objects.count() == 1:
            return True
        return False


@admin.register(Questions)
class QuestionsForm(admin.ModelAdmin):
    list_per_page = 10000000

    def has_add_permission(self, request):
        if Questions.objects.count() == 0:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if Questions.objects.count() == 1:
            return True
        return False
