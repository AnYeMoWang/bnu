# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0005_doc_frame'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name='\u89c6\u9891\u6807\u9898')),
                ('image', models.ImageField(upload_to=b'images/', null=True, verbose_name='\u89c6\u9891\u5c01\u9762\u56fe')),
                ('description', models.CharField(max_length=255, verbose_name='\u89c6\u9891\u63cf\u8ff0')),
                ('link', models.CharField(max_length=255, verbose_name='\u89c6\u9891\u94fe\u63a5', blank=True)),
                ('submit_time', models.DateTimeField(auto_now_add=True, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
            ],
            options={
                'verbose_name_plural': '\u5b9e\u8df5\u98ce\u91c7',
            },
        ),
    ]
