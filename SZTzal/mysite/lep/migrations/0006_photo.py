# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-21 08:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lep', '0005_auto_20170220_2006'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('image', stdimage.models.StdImageField(upload_to='media/img')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arts', to=settings.AUTH_USER_MODEL, verbose_name='author')),
            ],
        ),
    ]
