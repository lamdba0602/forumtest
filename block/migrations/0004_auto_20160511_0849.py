# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('block', '0003_auto_20160511_0458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='block',
            name='block_description',
            field=models.CharField(max_length=100, verbose_name='\u677f\u5757\u63cf\u8ff0'),
        ),
        migrations.AlterField(
            model_name='block',
            name='block_name',
            field=models.CharField(max_length=30, verbose_name='\u7248\u672c\u540d\u79f0'),
        ),
    ]
