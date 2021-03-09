# Generated by Django 3.1.7 on 2021-03-08 16:40

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('message_board', '0002_auto_20210307_1358'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_post',
            name='likes',
            field=models.ManyToManyField(related_name='post', to=settings.AUTH_USER_MODEL),
        ),
    ]
