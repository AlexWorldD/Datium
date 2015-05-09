# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_groups', '0020_auto_20150502_2027'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='studentgroup',
            options={'permissions': (('view_timetable', 'Can see timetable of the group'), ('view_grouplist', 'Can see the list of students in the group'), ('view_news', 'Can see news of the group'), ('view_homeworks', 'Can see homeworks'), ('view_documents', 'Can see documents'), ('add_and_edit_news', 'Can add and edit news of the group'), ('add_and_edit_documents', 'Can add and edit documents'), ('post_comments', 'Can post comments'), ('add_and_edit_homeworks', 'Can add and edit homeworks'), ('add_and_edit_teachers', 'Can add and edit teachers'), ('add_and_edit_subjects', 'Can add and edit subjects'), ('edit_timetable', 'Can edit timetable'), ('edit_others_news_homeworks_documents', 'Can edit news, homeworks and documents created by other users'), ('change_permissions', 'Can change permissions'), ('delete_users', 'Can delete users'))},
        ),
        migrations.AlterField(
            model_name='student',
            name='avatar',
            field=models.ImageField(default='/static/images/avatars/default_avatar.png', upload_to='avatars'),
        ),
    ]
