# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('block', '0004_auto_20160511_0849'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='block',
            options={'verbose_name': '\u677f\u5757', 'verbose_name_plural': '\u677f\u5757'},
        ),
        migrations.RenameField(
            model_name='block',
            old_name='block_create_timestamp',
            new_name='create_timestamp',
        ),
        migrations.RenameField(
            model_name='block',
            old_name='block_last_update_timestamp',
            new_name='last_update_timestamp',
        ),
        migrations.RenameField(
            model_name='block',
            old_name='block_owner',
            new_name='owner',
        ),
        migrations.RemoveField(
            model_name='block',
            name='block_description',
        ),
        migrations.RemoveField(
            model_name='block',
            name='block_name',
        ),
        migrations.AddField(
            model_name='block',
            name='desc',
            field=models.CharField(default=datetime.datetime(2016, 5, 11, 9, 30, 43, 93171, tzinfo=utc), max_length=100, verbose_name='\u63cf\u8ff0'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='block',
            name='name',
            field=models.CharField(default=datetime.datetime(2016, 5, 11, 9, 31, 2, 155950, tzinfo=utc), max_length=30, verbose_name='\u540d\u79f0'),
            preserve_default=False,
        ),
    ]
