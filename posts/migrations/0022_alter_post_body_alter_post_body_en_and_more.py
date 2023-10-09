# Generated by Django 4.2.4 on 2023-10-04 08:12

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0021_post_body_en_post_body_fa_post_description_en_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='محتوای پست'),
        ),
        migrations.AlterField(
            model_name='post',
            name='body_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='محتوای پست'),
        ),
        migrations.AlterField(
            model_name='post',
            name='body_fa',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='محتوای پست'),
        ),
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='توضیح کوتاه پست'),
        ),
        migrations.AlterField(
            model_name='post',
            name='description_en',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='توضیح کوتاه پست'),
        ),
        migrations.AlterField(
            model_name='post',
            name='description_fa',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='توضیح کوتاه پست'),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True, max_length=255, null=True, verbose_name='اسلاگ'),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug_en',
            field=models.SlugField(allow_unicode=True, blank=True, max_length=255, null=True, verbose_name='اسلاگ'),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug_fa',
            field=models.SlugField(allow_unicode=True, blank=True, max_length=255, null=True, verbose_name='اسلاگ'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='عنوان'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title_en',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='عنوان'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title_fa',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='عنوان'),
        ),
    ]
