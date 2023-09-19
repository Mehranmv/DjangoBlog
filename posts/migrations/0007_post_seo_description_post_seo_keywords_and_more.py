# Generated by Django 4.2.4 on 2023-09-07 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_post_display_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='seo_description',
            field=models.CharField(default=models.CharField(max_length=120, verbose_name='توضیح کوتاه پست'), max_length=120, verbose_name='توضیح کوتاه پست'),
        ),
        migrations.AddField(
            model_name='post',
            name='seo_keywords',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='seo_title',
            field=models.CharField(default=models.CharField(max_length=255, verbose_name='عنوان'), max_length=255, verbose_name='عنوان'),
        ),
    ]