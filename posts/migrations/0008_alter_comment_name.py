# Generated by Django 4.2.4 on 2023-08-19 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_comment_alter_category_options_alter_post_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(max_length=100, verbose_name='نام*'),
        ),
    ]
