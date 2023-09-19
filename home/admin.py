from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from .models import MenuItem


@admin.register(MenuItem)
class MenuItemAdmin(DraggableMPTTAdmin):
    list_filter = ('slug',)
    search_fields = ('name', 'slug')
    prepopulated_fields = {
        'slug': ('name',),
    }
