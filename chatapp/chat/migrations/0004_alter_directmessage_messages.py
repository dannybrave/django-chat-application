# Generated by Django 3.2.3 on 2021-05-24 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_auto_20210523_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='directmessage',
            name='messages',
            field=models.ManyToManyField(to='chat.Message', verbose_name='Private Messages'),
        ),
    ]
