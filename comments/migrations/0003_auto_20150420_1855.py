# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_auto_20150420_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentstable',
            name='content_type',
            field=models.ForeignKey(to='contenttypes.ContentType', blank=True),
        ),
        migrations.AlterField(
            model_name='commentstable',
            name='object_id',
            field=models.PositiveIntegerField(blank=True),
        ),
    ]
