# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_groups', '0007_auto_20150413_1125'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='studentgroup',
            options={'permissions': (('view_timetable', 'Can see timetable of the group'), ('view_grouplist', 'Can see the list of students in the group'), ('view_news', 'Can see news of the group'), ('view_homeworks', 'Can see homeworks'), ('view_documents', 'Can see documents'), ('add_and_edit_news', 'Can add and edit news of the group'), ('add_and_edit_homeworks', 'Can add and edit homeworks'), ('add_and_edit_documents', 'Can add and edit documents'))},
        ),
    ]
