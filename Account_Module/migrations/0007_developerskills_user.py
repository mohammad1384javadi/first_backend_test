# Generated by Django 4.2.6 on 2023-10-15 14:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Account_Module', '0006_developerskills_user_field_user_skill'),
    ]

    operations = [
        migrations.AddField(
            model_name='developerskills',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر'),
        ),
    ]
