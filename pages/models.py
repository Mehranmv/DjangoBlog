# django imports
from django.db import models
from django.utils.translation import gettext_lazy as _
# locale imports
from utils import AbstractDateTime
# third party imports
from ckeditor_uploader.fields import RichTextUploadingField


class AboutUs(AbstractDateTime):
    title = models.CharField(
        max_length=100,
        verbose_name=_("عنوان صفحه")
    )
    slug = models.SlugField(
        max_length=100,
        verbose_name=_("اسلاگ"),
        allow_unicode=True
    )
    description = RichTextUploadingField(
        verbose_name=_("محتوای صفحه")
    )

    class Meta:
        verbose_name = _("درباره ما")
        verbose_name_plural = _("درباره ما")

    def __str__(self):
        return self.title

    @classmethod
    def create_or_get_default(cls):
        """
        this is for when we don't have page
        """
        record = cls.objects.last()
        if record:
            return record
        return cls.objects.create(title='درباره ما', slug='aboutus', description='تست')


class ContactUs(AbstractDateTime):
    title = models.CharField(
        max_length=100,
        verbose_name=_("عنوان صفحه")
    )
    slug = models.SlugField(
        max_length=100,
        verbose_name=_("اسلاگ"),
        allow_unicode=True
    )
    description = RichTextUploadingField(
        verbose_name=_("محتوای صفحه")
    )

    class Meta:
        verbose_name = _("تماس با ما")
        verbose_name_plural = _("تماس با ما")

    def __str__(self):
        return self.title

    @classmethod
    def create_or_get_default(cls):
        record = cls.objects.last()
        if record:
            return record
        return cls.objects.create(title='تماس با ما', slug='contactus', description='تماس با ما')


class Questions(AbstractDateTime):
    title = models.CharField(
        max_length=100,
        verbose_name=_("عنوان صفحه")
    )
    slug = models.SlugField(
        max_length=100,
        verbose_name=_("اسلاگ"),
        allow_unicode=True
    )
    description = RichTextUploadingField(
        verbose_name=_("محتوای صفحه")
    )

    class Meta:
        verbose_name = _("پرسش های متداول")
        verbose_name_plural = _("پرسش های متداول")

    def __str__(self):
        return self.title

    @classmethod
    def create_or_get_default(cls):
        record = cls.objects.last()
        if record:
            return record
        return cls.objects.create(title='سوالات متداول', slug='questions', description='سوالات متداول')


class Rules(AbstractDateTime):
    title = models.CharField(
        max_length=100,
        verbose_name=_("عنوان صفحه")
    )
    slug = models.SlugField(
        max_length=100,
        verbose_name=_("اسلاگ"),
        allow_unicode=True
    )
    description = RichTextUploadingField(
        verbose_name=_("محتوای صفحه")
    )

    class Meta:
        verbose_name = _("قوانین")
        verbose_name_plural = _("قوانین")

    def __str__(self):
        return self.title

    @classmethod
    def create_or_get_default(cls):
        record = cls.objects.last()
        if record:
            return record
        return cls.objects.create(title='قوانین', slug='rules', description='فوانین')
