# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0002_auto_20160425_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='practice',
            name='type',
            field=models.IntegerField(default=0, verbose_name='\u5206\u7c7b', choices=[(0, '\u5168\u90e8'), (1, '\u5f18\u6587\u52b1\u6559'), (2, '\u793e\u4f1a\u89c2\u5bdf'), (3, '\u7f8e\u4e3d\u4e2d\u56fd'), (4, '\u804c\u6daf\u4f53\u9a8c'), (5, '\u94ed\u8bb0\u5386\u53f2')]),
        ),
    ]
