# Generated by Django 3.2.3 on 2021-05-24 23:45

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0006_allchats'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AllChats',
            new_name='AllChat',
        ),
    ]
