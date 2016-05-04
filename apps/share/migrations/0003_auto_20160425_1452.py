# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0002_auto_20160425_1405'),
    ]

    operations = [
        migrations.AddField(
            model_name='downloads',
            name='title',
            field=models.CharField(default='', max_length=50, verbose_name='\u6587\u4ef6\u6807\u9898'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='downloads',
            name='name',
            field=models.FileField(max_length=255, upload_to=b'downloads/'),
        ),
    ]
