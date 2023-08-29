# Generated by Django 4.2.4 on 2023-08-19 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0012_alter_comment_body_alter_comment_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='categories',
        ),
        migrations.AddField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(related_name='cpost', to='posts.category'),
        ),
    ]