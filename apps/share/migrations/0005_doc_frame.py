# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0004_parentlessons_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doc',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name='\u8d44\u6599\u6807\u9898')),
                ('name', models.FileField(max_length=255, upload_to=b'downloads/')),
                ('submit_time', models.DateTimeField(auto_now_add=True, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
            ],
            options={
                'verbose_name_plural': '\u652f\u6559\u8d44\u6599\u5e93',
            },
        ),
        migrations.CreateModel(
            name='Frame',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name='\u6807\u9898')),
                ('content', models.TextField(verbose_name='\u6b63\u6587\u5185\u5bb9')),
                ('submit_time', models.DateTimeField(auto_now_add=True, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
                ('update_time', models.DateTimeField(auto_now_add=True, verbose_name='\u4fee\u6539\u65f6\u95f4')),
                ('view_count', models.IntegerField(default=0, verbose_name='\u6d4f\u89c8\u6b21\u6570')),
            ],
            options={
                'verbose_name_plural': '\u8bfe\u7a0b\u6846\u67b6',
            },
        ),
    ]
