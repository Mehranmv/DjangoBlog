# Django imports
from django.core.paginator import Paginator
from django.db import models
from django.utils.translation import gettext_lazy as _
# third party imports
from jalali_date import datetime2jalali


def pagination(data, page_number, page_size=10):
    paginator = Paginator(data, page_size)
    page = paginator.get_page(page_number)
    return page


class AbstractDateTime(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def created_jalali(self):
        return datetime2jalali(self.created)

    def updated_jalali(self):
        return datetime2jalali(self.updated)


class SEO(models.Model):
    seo_title = models.CharField(
        max_length=255,
        verbose_name=_('عنوان'),
    )
    seo_description = models.CharField(
        max_length=120,
        verbose_name=_('توضیح کوتاه پست'),
    )
    seo_keywords = models.CharField(
        max_length=255,
        verbose_name=_("کلمات کلیدی"),
        default=_("بازی  - بازی اندروید  - برنامه اندروید - نقد و بررسی - فیم و سریال"),
        blank=True,
        null=True
    )

    class Meta:
        abstract = True
