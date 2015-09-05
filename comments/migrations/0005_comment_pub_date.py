# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0004_auto_20150420_2300'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published', auto_now_add=True, default='2015-05-10 0:52:0'),
            preserve_default=False,
        ),
    ]
