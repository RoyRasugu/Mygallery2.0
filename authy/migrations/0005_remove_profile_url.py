# Generated by Django 2.2 on 2021-10-20 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authy', '0004_auto_20211020_1442'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='url',
        ),
    ]