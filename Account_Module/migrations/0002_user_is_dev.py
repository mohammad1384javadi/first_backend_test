# Generated by Django 4.2.6 on 2023-10-13 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account_Module', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_dev',
            field=models.BooleanField(default=False, verbose_name='توسعه دهنده سایت'),
        ),
    ]