from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from .models import MenuItem


@admin.register(MenuItem)
class MenuItemAdmin(DraggableMPTTAdmin):
    list_filter = ('slug_fa',)
    search_fields = ('title_fa', 'slug_fa')
    prepopulated_fields = {
        'slug_fa': ('title_fa',),
        'slug_en': ("title_en",),
    }
    fieldsets = (
        (
            None, {
                'fields': [
                    'title_fa',
                    'slug_fa',
                    'title_en',
                    'slug_en',
                    'link',
                    'parent'
                ]
            }
        ),
    )
