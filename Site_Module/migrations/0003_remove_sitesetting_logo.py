# Generated by Django 4.2.6 on 2023-10-14 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Site_Module', '0002_alter_sitesetting_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sitesetting',
            name='logo',
        ),
    ]
