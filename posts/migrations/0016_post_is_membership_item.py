# Generated by Django 4.2.4 on 2023-09-24 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0015_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_membership_item',
            field=models.BooleanField(default=False, verbose_name='برای اکانت های ویژه'),
        ),
    ]
