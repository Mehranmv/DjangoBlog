from django.contrib import admin
from .models import Coupon, Membership
from django.utils.translation import gettext_lazy as _

admin.site.register(Coupon)
admin.site.register(Membership)
