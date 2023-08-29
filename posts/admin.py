from django.contrib import admin
from .models import Category, Post, Comment
from mptt.admin import MPTTModelAdmin


@admin.register(Category)
class CategoryAdmin(MPTTModelAdmin):
    list_display = ('name', 'slug', 'is_sub')
    prepopulated_fields = {
        'slug': ('name',),
    }


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'categories',)
    prepopulated_fields = {
        'slug': ('title',),
    }
    raw_id_fields = ('categories',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body'[:40], 'is_accepted')
