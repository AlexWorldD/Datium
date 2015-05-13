# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_groups', '0021_auto_20150509_2013'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentgroup',
            name='entrance_year',
            field=models.IntegerField(default=2013),
            preserve_default=False,
        ),
    ]
