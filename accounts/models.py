from django.db import models
from django.contrib.auth.models import User
from utils import AbstractDateTime
from django.utils.text import gettext_lazy as _
from django.core.exceptions import ValidationError


class Coupon(AbstractDateTime):
    code = models.CharField(
        max_length=50,
        verbose_name=_("کد")
    )
    amount = models.IntegerField(
        verbose_name=_("مفدار تخفیف")
    )
    is_percentage = models.BooleanField(
        verbose_name=_("درصدی")
    )
    is_amount = models.BooleanField(
        verbose_name=_("مبلغی")
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

    @classmethod
    def discount(cls, code):
        coupon = cls.objects.get(code=code)
        amount = 10000
        amount_2 = 20000
        if coupon.is_percentage:
            a1 = 10000 * coupon.amount * 0.01
            a2 = 20000 * coupon.amount * 0.01
            if coupon.use_limit == 0:
                raise ValidationError(_("Code is expired"), code="invalid")
            elif coupon.amount == 100:
                amount = 0
                amount_2 = 0
                coupon.use_limit -= 1
                coupon.save()
                return amount, amount_2
            elif coupon.tantamount is not None and a1 > coupon.tantamount:
                amount = 10000 - coupon.tantamount
                amount_2 = 20000 - coupon.tantamount
                coupon.use_limit -= 1
                coupon.save()
                return amount, amount_2
            else:
                amount -= a1
                amount_2 -= a2
                coupon.use_limit -= 1
                coupon.save()
                return amount, amount_2

        else:
            if coupon.use_limit == 0:
                raise ValidationError(_("Code is expired"), code="invalid")
            if coupon.is_amount:
                amount -= coupon.amount
                amount_2 -= coupon.amount
                coupon.use_limit -= 1
                coupon.save()
                return amount, amount_2


class Membership(AbstractDateTime):
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
