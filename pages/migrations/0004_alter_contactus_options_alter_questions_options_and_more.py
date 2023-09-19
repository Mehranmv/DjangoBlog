# Generated by Django 4.2.4 on 2023-09-17 13:06

import ckeditor_uploader.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_contactus_questions_rules'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactus',
            options={'verbose_name': 'تماس با ما', 'verbose_name_plural': 'تماس با ما'},
        ),
        migrations.AlterModelOptions(
            name='questions',
            options={'verbose_name': 'پرسش های متداول', 'verbose_name_plural': 'پرسش های متداول'},
        ),
        migrations.AlterModelOptions(
            name='rules',
            options={'verbose_name': 'قوانین', 'verbose_name_plural': 'قوانین'},
        ),
        migrations.AddField(
            model_name='aboutus',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aboutus',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='contactus',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contactus',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='questions',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='questions',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='rules',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rules',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='محتوای صفحه'),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='slug',
            field=models.SlugField(allow_unicode=True, max_length=100, verbose_name='اسلاگ'),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='title',
            field=models.CharField(max_length=100, verbose_name='عنوان صفحه'),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='محتوای صفحه'),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='slug',
            field=models.SlugField(allow_unicode=True, max_length=100, verbose_name='اسلاگ'),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='title',
            field=models.CharField(max_length=100, verbose_name='عنوان صفحه'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='محتوای صفحه'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='slug',
            field=models.SlugField(allow_unicode=True, max_length=100, verbose_name='اسلاگ'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='title',
            field=models.CharField(max_length=100, verbose_name='عنوان صفحه'),
        ),
        migrations.AlterField(
            model_name='rules',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='محتوای صفحه'),
        ),
        migrations.AlterField(
            model_name='rules',
            name='slug',
            field=models.SlugField(allow_unicode=True, max_length=100, verbose_name='اسلاگ'),
        ),
        migrations.AlterField(
            model_name='rules',
            name='title',
            field=models.CharField(max_length=100, verbose_name='عنوان صفحه'),
        ),
    ]
