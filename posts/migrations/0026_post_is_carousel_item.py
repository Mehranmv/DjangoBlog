# Generated by Django 4.2.4 on 2023-09-04 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0025_remove_comment_accepted_comment_is_accepted'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_carousel_item',
            field=models.BooleanField(default=False, verbose_name='نمایش در کاروسل'),
        ),
    ]