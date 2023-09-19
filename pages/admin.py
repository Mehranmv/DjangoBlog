from django.contrib import admin
from .models import AboutUs, ContactUs, Rules, Questions
from .forms import AboutUsForm, ContactUsForm, RulesForm, QuestionsForm

admin.site.register(AboutUs, AboutUsForm)

admin.site.register(ContactUs, ContactUsForm)
admin.site.register(Rules, RulesForm)
admin.site.register(Questions, QuestionsForm)
