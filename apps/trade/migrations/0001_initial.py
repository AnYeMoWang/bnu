# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.IntegerField(default=1, verbose_name='\u5206\u7c7b', choices=[(1, '\u65b0\u95fb'), (2, '\u516c\u544a')])),
                ('title', models.CharField(max_length=50, verbose_name='\u65b0\u95fb\u6807\u9898')),
                ('content', models.TextField(verbose_name=b'\xe6\xad\xa3\xe6\x96\x87\xe5\x86\x85\xe5\xae\xb9')),
                ('submit_time', models.DateTimeField(auto_now_add=True, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
                ('update_time', models.DateTimeField(auto_now_add=True, verbose_name='\u4fee\u6539\u65f6\u95f4')),
            ],
            options={
                'verbose_name_plural': '\u65b0\u95fb/\u516c\u544a',
            },
        ),
    ]
