from modeltranslation.translator import translator, TranslationOptions
from .models import Post, Category


class PostTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'description',
        'slug',
        'body'
    )


class CategoryTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'slug',
    )


translator.register(Post, PostTranslationOptions)
translator.register(Category, CategoryTranslationOptions)
