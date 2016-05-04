# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChildLessons',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name='\u6807\u9898')),
                ('link', models.CharField(max_length=255, verbose_name='\u7f51\u8bfe\u94fe\u63a5')),
                ('submit_time', models.DateTimeField(auto_now_add=True, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
                ('update_time', models.DateTimeField(auto_now_add=True, verbose_name='\u4fee\u6539\u65f6\u95f4')),
            ],
            options={
                'verbose_name_plural': '\u5b50\u8bfe\u7a0b',
            },
        ),
        migrations.CreateModel(
            name='Downloads',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.FileField(max_length=255, upload_to=b'/Users/SH/workspace/bnu/bnu/server_config/media')),
                ('link', models.CharField(max_length=255)),
                ('submit_time', models.DateTimeField(auto_now_add=True, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
                ('update_time', models.DateTimeField(auto_now_add=True, verbose_name='\u4fee\u6539\u65f6\u95f4')),
            ],
            options={
                'verbose_name_plural': '\u5e38\u7528\u4e0b\u8f7d',
            },
        ),
        migrations.CreateModel(
            name='ParentLessons',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name='\u6807\u9898')),
                ('description', models.CharField(max_length=255, verbose_name='\u8bfe\u7a0b\u63cf\u8ff0')),
                ('submit_time', models.DateTimeField(auto_now_add=True, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
                ('update_time', models.DateTimeField(auto_now_add=True, verbose_name='\u4fee\u6539\u65f6\u95f4')),
            ],
            options={
                'verbose_name_plural': '\u4e3b\u8bfe\u7a0b',
            },
        ),
        migrations.AddField(
            model_name='childlessons',
            name='parent',
            field=models.ForeignKey(to='share.ParentLessons'),
        ),
    ]
