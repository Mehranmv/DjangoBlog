# Generated by Django 4.2.4 on 2023-08-24 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0022_alter_category_is_sub_alter_category_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='is_reply',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='reply',
        ),
    ]
