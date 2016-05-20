# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('block_name', models.CharField(max_length=30)),
                ('block_description', models.IntegerField()),
                ('block_create_timestamp', models.DateTimeField(auto_now_add=True)),
                ('block_last_update_timestamp', models.DateTimeField(auto_now=True)),
                ('block_owner', models.ForeignKey(verbose_name=b'\xe4\xbd\x9c\xe8\x80\x85', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
