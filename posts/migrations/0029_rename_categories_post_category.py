# Generated by Django 4.2.4 on 2023-09-04 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0028_alter_comment_post_alter_post_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='categories',
            new_name='category',
        ),
    ]
