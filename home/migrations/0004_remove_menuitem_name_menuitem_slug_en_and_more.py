# Generated by Django 4.2.4 on 2023-10-04 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_menuitem_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='name',
        ),
        migrations.AddField(
            model_name='menuitem',
            name='slug_en',
            field=models.SlugField(allow_unicode=True, blank=True, null=True, unique=True, verbose_name='اسلاگ'),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='slug_fa',
            field=models.SlugField(allow_unicode=True, blank=True, null=True, unique=True, verbose_name='اسلاگ'),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='نام'),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='title_en',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='نام'),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='title_fa',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True, null=True, unique=True, verbose_name='اسلاگ'),
        ),
    ]