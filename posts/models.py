# Django imports
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.shortcuts import reverse
# local imports
from .managers import CommentManager, PostManager
# Third party packages import
from mptt.models import MPTTModel, TreeForeignKey
from ckeditor_uploader.fields import RichTextUploadingField
from utils import DT, SEO
from star_ratings.models import Rating


class Category(MPTTModel, DT):
    name = models.CharField(
        max_length=50,
        verbose_name=_("نام")
    )
    slug = models.SlugField(
        unique=True,
        allow_unicode=True,
        verbose_name=_("اسلاگ")
    )
    is_sub = models.BooleanField(
        default=False,
        verbose_name=_("زیر مجموعه")
    )
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name = _('دسته بندی')
        verbose_name_plural = _('دسته بندی ها')

    def __str__(self):
        return self.name


def get_absolute_url(self):
    return reverse('posts:category', args=[self.slug])


class Post(DT, SEO):
    STATUS_CHOICES = (
        ('scheduled', 'Scheduled'),
        ('published', 'Published'),
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=_("کاریر"),
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name=_('دسته بندی')

    )
    title = models.CharField(
        max_length=255,
        verbose_name=_('عنوان'),
    )
    description = models.CharField(
        max_length=120,
        verbose_name=_('توضیح کوتاه پست')
    )
    slug = models.SlugField(
        allow_unicode=True,
        max_length=255,
        verbose_name=_("اسلاگ")
    )
    thumbnail = models.ImageField(
        upload_to="post/",
        verbose_name=_("تصویر پست")
    )
    body = RichTextUploadingField(
        verbose_name=_("محتوای پست")
    )
    is_carousel_item = models.BooleanField(
        default=False,
        verbose_name=_("نمایش در کاروسل")
    )
    display_post = models.BooleanField(
        default=True,
        verbose_name=_("نمایش پست")
    )
    publish_date = models.DateTimeField(
        verbose_name=_("زمان انتشار"),
        null=True,
        blank=True,
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='published'
    )

    objects = PostManager()

    class Meta:
        verbose_name = _('پست')
        verbose_name_plural = _('پست ها')
        ordering = ('-updated',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('posts:post_detail', args=[self.slug])


def average_rating(self):
    ratings = Rating.objects.filter(object_id=self.id, content_type__model='post')
    return ratings.aggregate(models.Avg('rating'))['rating__avg']


class Comment(MPTTModel, DT):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
    )

    name = models.CharField(
        max_length=100,
        verbose_name=_('نام')

    )

    email = models.EmailField(
        verbose_name=_('ایمیل')
    )

    body = models.TextField(
        verbose_name=_('نظر')
    )
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='replies'
    )
    is_accepted = models.BooleanField(
        default=False,
        verbose_name=_("تایید شده")
    )
    objects = CommentManager()

    class MPTTMeta:
        order_insertion_by = ['id']

    class Meta:
        verbose_name = _('دیدگاه')
        verbose_name_plural = _(' دیدگاه ها')

    def __str__(self):
        return f'{self.email} - {self.name}'

    def like_count(self):
        return self.clike.count()


class Bookmark(DT):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE
    )


class Like(DT):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ulike')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="clike")

    def __str__(self):
        return {self.comment}


