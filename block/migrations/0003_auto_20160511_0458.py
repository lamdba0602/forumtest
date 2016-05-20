# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('block', '0002_auto_20160511_0430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='block',
            name='block_owner',
            field=models.ForeignKey(verbose_name='\u4f5c\u8005', to=settings.AUTH_USER_MODEL),
        ),
    ]
