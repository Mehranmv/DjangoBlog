# Generated by Django 4.2.4 on 2023-10-04 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0022_alter_post_body_alter_post_body_en_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='name_en',
            field=models.CharField(max_length=50, null=True, verbose_name='نام'),
        ),
        migrations.AddField(
            model_name='category',
            name='name_fa',
            field=models.CharField(max_length=50, null=True, verbose_name='نام'),
        ),
        migrations.AddField(
            model_name='category',
            name='slug_en',
            field=models.SlugField(allow_unicode=True, null=True, unique=True, verbose_name='اسلاگ'),
        ),
        migrations.AddField(
            model_name='category',
            name='slug_fa',
            field=models.SlugField(allow_unicode=True, null=True, unique=True, verbose_name='اسلاگ'),
        ),
    ]