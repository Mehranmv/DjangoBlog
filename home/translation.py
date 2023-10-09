from modeltranslation.translator import translator, TranslationOptions
from .models import MenuItem


class MenuTranslationOptions(TranslationOptions):
    """
    this is to create fields for fa and en languages for translating posts into this languages
    using django-modeltranslation
    """
    fields = (
        'title',
        'slug',
    )


translator.register(MenuItem, MenuTranslationOptions)
