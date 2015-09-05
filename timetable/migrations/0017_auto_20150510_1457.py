# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0016_auto_20150510_0053'),
    ]

    operations = [
        migrations.RenameField(
            model_name='timetable',
            old_name='student_group',
            new_name='group',
        ),
        migrations.AddField(
            model_name='lesson',
            name='semester',
            field=models.IntegerField(default=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='timetable',
            name='semester',
            field=models.IntegerField(default=4),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='lesson',
            unique_together=set([('group', 'semester', 'day', 'class_number')]),
        ),
        migrations.AlterUniqueTogether(
            name='timetable',
            unique_together=set([('group', 'semester')]),
        ),
    ]
