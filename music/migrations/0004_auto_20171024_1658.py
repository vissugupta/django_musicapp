# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-24 11:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_song_is_fav'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_icon',
            field=models.FileField(max_length=150, upload_to=''),
        ),
    ]
