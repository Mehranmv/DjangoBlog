# Generated by Django 4.2.4 on 2023-09-23 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_coupon_code_alter_coupon_discount_amount_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coupon',
            options={'verbose_name': 'کد تخفیف', 'verbose_name_plural': 'کد تخفیف'},
        ),
        migrations.AlterModelOptions(
            name='membership',
            options={'verbose_name': 'حساب ویژه', 'verbose_name_plural': 'حساب ویژه'},
        ),
    ]
