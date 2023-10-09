# django imports
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
# locale imports
from .models import Category, Post, Comment
# third party imports
from mptt.admin import MPTTModelAdmin


@admin.register(Category)
class CategoryAdmin(MPTTModelAdmin):
    list_display = ('title_fa', 'slug_fa', 'is_sub')
    prepopulated_fields = {
        'slug_fa': ('title_fa',),
        'slug_en': ('title_en',),

    }
    search_fields = ('title_fa', 'slug_fa')
    list_filter = ('is_sub',)

    fieldsets = [
        (
            _("اسم دسته بندی"),
            {
                'fields': [
                    'title_fa',
                    'title_en',
                ],
            }
        ),
        (
            _("اسلاگ دسته بندی"),
            {
                'fields': [
                    'slug_fa',
                    'slug_en',
                ],
            }
        ),
        (
            _("تنظیمات دسته بندی ها"),
            {
                'fields': [
                    'is_sub',
                    'parent'
                ]
            }
        )
    ]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title_fa', 'user', 'category',)
    list_filter = ('category',)
    search_fields = ('title_fa', 'body_fa')
    prepopulated_fields = {
        'slug_fa': ('title_fa',),
        'slug_en': ("title_en",),
    }
    raw_id_fields = ('category', 'user')
    fieldsets = [
        (
            None,
            {
                "fields": ["user", "category"],
            },
        ),

        (
            _("عنوان و اسلاگ فارسی"),
            {
                "fields": ["title_fa", "slug_fa", "description_fa"],
            },
        ),
        (
            _("عنوان و اسلاگ انگلیسی "),
            {
                "fields": ["title_en", "slug_en", "description_en"],
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
                "fields": ["body_fa", "body_en"],
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
                "fields": ["is_carousel_item", "display_post", "is_membership_item"],
            }
        )
    ]

    @admin.action(description=_("نمایش در کاروسل"))
    def enable_in_carousel(self, request, queryset):
        queryset.update(is_carousel_item=True)

    @admin.action(description=_(" عدم نمایش در کاروسل"))
    def disable_in_carousel(self, request, queryset):
        queryset.update(is_carousel_item=False)

    actions = [enable_in_carousel, disable_in_carousel]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body'[:40], 'is_accepted')
    list_filter = ('is_accepted',)
    search_fields = ('name', 'body')
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

    @admin.action(description=_("تایید کردن دیدگاه ها"))
    def make_accepted(self, request, queryset):
        queryset.update(is_accepted=True)

    actions = [make_accepted]
