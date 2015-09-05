# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0003_auto_20150420_1855'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='commentstable',
            unique_together=set([('content_type', 'object_id')]),
        ),
    ]
