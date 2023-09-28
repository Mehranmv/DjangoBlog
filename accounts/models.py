from django.db import models
from django.contrib.auth.models import User
from utils import DT
from django.utils.text import gettext_lazy as _


class Coupon(DT):
    code = models.CharField(
        max_length=50,
        verbose_name=_("کد")
    )
    discount_percentage = models.FloatField(
        null=True,
        blank=True,
        default=None,
        verbose_name=_("درصد تخفیف")
    )
    discount_amount = models.IntegerField(
        null=True,
        blank=True,
        default=None,

        verbose_name=_("مبلغ تخفیف")
    )
    tantamount = models.IntegerField(
        blank=True,
        null=True,
        default=None,

        verbose_name=_("سقف مبلع تخفیف")
    )
    use_limit = models.IntegerField(
        blank=True,
        null=True,
        default=None,

        verbose_name=_("تعداد استفاده")
    )

    class Meta:
        verbose_name = _("کد تخفیف")
        verbose_name_plural = _("کد تخفیف")

    def __str__(self):
        return f"{self.code}"


class Membership(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )
    start_date = models.DateField(
        auto_now_add=True
    )
    end_date = models.DateField()
    plan_type = models.CharField(
        max_length=50
    )
    coupon = models.ForeignKey(
        Coupon,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = _("حساب ویژه")
        verbose_name_plural = _("حساب ویژه")

    def __str__(self):
        return self.user.username
