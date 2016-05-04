# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0002_trade_view_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trade',
            name='title',
            field=models.CharField(max_length=50, verbose_name='\u6807\u9898'),
        ),
        migrations.AlterField(
            model_name='trade',
            name='view_count',
            field=models.IntegerField(default=0, verbose_name='\u6d4f\u89c8\u6b21\u6570'),
        ),
    ]
