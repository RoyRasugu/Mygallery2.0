# Generated by Django 2.2 on 2021-10-17 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_likes'),
        ('authy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='favorites',
            field=models.ManyToManyField(to='post.Post'),
        ),
    ]
