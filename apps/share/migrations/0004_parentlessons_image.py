# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0003_auto_20160425_1452'),
    ]

    operations = [
        migrations.AddField(
            model_name='parentlessons',
            name='image',
            field=models.ImageField(upload_to=b'images/', null=True, verbose_name='\u8bfe\u7a0b\u5c01\u9762\u56fe'),
        ),
    ]
