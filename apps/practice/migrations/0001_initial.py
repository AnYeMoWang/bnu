# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Practice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.IntegerField(default=1, verbose_name='\u5206\u7c7b', choices=[(1, '\u5f18\u6587\u52b1\u6559'), (2, '\u793e\u4f1a\u89c2\u5bdf'), (3, '\u7f8e\u4e3d\u4e2d\u56fd'), (4, '\u804c\u6daf\u4f53\u9a8c'), (5, '\u94ed\u8bb0\u5386\u53f2')])),
                ('title', models.CharField(max_length=50, verbose_name='\u65b0\u95fb\u6807\u9898')),
                ('content', models.TextField(verbose_name='\u6b63\u6587\u5185\u5bb9')),
                ('submit_time', models.DateTimeField(auto_now_add=True, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
                ('update_time', models.DateTimeField(auto_now_add=True, verbose_name='\u4fee\u6539\u65f6\u95f4')),
                ('view_count', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': '\u5b9e\u8df5\u5185\u5bb9',
            },
        ),
    ]
