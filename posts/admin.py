from django.contrib import admin
from .models import Category, Post, Comment, Bookmark
from mptt.admin import MPTTModelAdmin
from django.utils.translation import gettext_lazy as _
from modeltranslation.admin import TranslationAdmin

admin.site.register(Bookmark)


@admin.action(description=_("تایید کردن دیدگاه ها"))
def make_accepted(self, request, queryset):
    queryset.update(is_accepted=True)


@admin.action(description=_("نمایش در کاروسل"))
def enable_in_carousel(self, request, queryset):
    queryset.update(is_carousel_item=True)


@admin.action(description=_(" عدم نمایش در کاروسل"))
def disable_in_carousel(self, request, queryset):
    queryset.update(is_carousel_item=False)


@admin.register(Category)
class CategoryAdmin(MPTTModelAdmin):
    list_display = ('name', 'slug', 'is_sub')
    prepopulated_fields = {
        'slug': ('name',),
    }
    search_fields = ('name', 'slug')
    list_filter = ('is_sub',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'category',)
    list_filter = ('category',)
    search_fields = ('title', 'body')
    prepopulated_fields = {
        'slug': ('title',),
        'seo_title': ('title',),
        "seo_description": ('description',)
    }
    actions = [enable_in_carousel, disable_in_carousel]
    raw_id_fields = ('category', 'user')
    fieldsets = [
        (
            None,
            {
                "fields": ["user", "category"],
            },
        ),

        (
            _("عنوان و اسلاگ"),
            {
                "fields": ["title", "slug", "description"],

            }
        ),
        (
            _("تصویر پست"),
            {
                "fields": ['thumbnail'],
            }
        ),
        (
            _("محتوای پست"),
            {
                "fields": ["body"],
            },
        ),
        (
            _(" زمانبندی انتشار"),
            {
                "fields": ["publish_date", "status"],
            }
        ),
        (
            _("تنظیمات سئو"),
            {
                "fields": ["seo_title", "seo_description", "seo_keywords"],
            }
        ),
        (
            _("تنظیمات نمایش "),
            {
                "fields": ["is_carousel_item", "display_post"],
            }
        )
    ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body'[:40], 'is_accepted')
    list_filter = ('is_accepted',)
    search_fields = ('name', 'body')
    actions = [make_accepted]
    fieldsets = [
        (
            None,
            {
                "fields": ["post"],
            },
        ),
        (
            _("نام و ایمیل"),
            {
                "fields": ["name", 'email']
            }
        ),
        (
            _("نظر"),
            {
                "fields": ["body"]
            }
        ),
        (
            _("تایید کردن"),
            {
                'fields': ["is_accepted"]
            }
        ),
        (
            _("ریپلای"),
            {
                "fields": ['parent']
            }
        )
    ]
