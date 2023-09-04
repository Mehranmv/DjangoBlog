from django.contrib import admin
from .models import Category, Post, Comment
from mptt.admin import MPTTModelAdmin
from django.utils.translation import gettext_lazy as _


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
    }
    actions = [enable_in_carousel,disable_in_carousel]
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
                "classes": ["collapse"],
                "fields": ["title", "slug", "description"],

            }
        ),
        (
            _("تصویر پست"),
            {
                "classes": ["collapse"],
                "fields": ['thumbnail'],
            }
        ),
        (
            _("محتوای پست"),
            {
                "classes": ["collapse"],
                "fields": ["body"],
            },
        ),
        (
            _("نمایش در کاروسل"),
            {
                "classes": ["collapse"],
                "fields": ["is_carousel_item"],
            }
        )
    ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body'[:40], 'is_accepted')
    list_filter = ('is_accepted',)
    search_fields = ('name', 'body')
    actions = [make_accepted]
