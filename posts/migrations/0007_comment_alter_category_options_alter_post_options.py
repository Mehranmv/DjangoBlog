# Generated by Django 4.2.4 on 2023-08-19 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_alter_post_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='نام')),
                ('email', models.EmailField(max_length=254, verbose_name='ایمیل*')),
                ('body', models.TextField(verbose_name='نظر*')),
            ],
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'دسته بندی', 'verbose_name_plural': 'دسته بندی ها'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'پست', 'verbose_name_plural': 'پست ها'},
        ),
    ]
