# Generated by Django 4.2.4 on 2023-08-22 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0020_comment_is_reply_comment_reply'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='updated_for_xml',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
