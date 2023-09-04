# Django imports
from django.core.paginator import Paginator
from django.db import models
from jalali_date import datetime2jalali


def pagination(data, page_number, page_size=10):
    paginator = Paginator(data, page_size)
    page = paginator.get_page(page_number)
    return page


class DT(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def created_jalali(self):
        return datetime2jalali(self.created)

    def updated_jalali(self):
        return datetime2jalali(self.updated)
