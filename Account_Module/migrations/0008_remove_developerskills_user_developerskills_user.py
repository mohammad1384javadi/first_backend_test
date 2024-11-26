# Generated by Django 4.2.6 on 2023-10-15 14:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account_Module', '0007_developerskills_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='developerskills',
            name='user',
        ),
        migrations.AddField(
            model_name='developerskills',
            name='user',
            field=models.ManyToManyField(null=True, to=settings.AUTH_USER_MODEL, verbose_name='کاربر'),
        ),
    ]
