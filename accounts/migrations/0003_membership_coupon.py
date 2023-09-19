# Generated by Django 4.2.4 on 2023-09-19 06:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_coupon'),
    ]

    operations = [
        migrations.AddField(
            model_name='membership',
            name='coupon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.coupon'),
        ),
    ]