# Generated by Django 4.2.4 on 2023-08-19 18:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0015_post_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.ForeignKey(auto_created=True, on_delete=django.db.models.deletion.CASCADE, related_name='upost', to=settings.AUTH_USER_MODEL, verbose_name='کاریر'),
        ),
    ]