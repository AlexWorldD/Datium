# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_groups', '0012_auto_20150420_1505'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='comments',
        ),
        migrations.RemoveField(
            model_name='news',
            name='comments',
        ),
    ]
