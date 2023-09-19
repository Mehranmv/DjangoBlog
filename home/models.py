from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.translation import gettext_lazy as _


class MenuItem(MPTTModel):
    name = models.CharField(
        max_length=100,
        verbose_name=_("نام")
    )
    slug = models.SlugField(
        unique=True,
        allow_unicode=True,
        verbose_name=_("اسلاگ")
    )
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name = _('منو')
        verbose_name_plural = _('منو')
    def __str__(self):
        return self.name
