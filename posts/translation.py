from modeltranslation.translator import translator, TranslationOptions
from .models import Post


class PostTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'description',
        'slug',
        'body'
    )


translator.register(Post, PostTranslationOptions)
