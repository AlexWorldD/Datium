# -*- coding: utf-8 -*-
from django.contrib.auth.models import User, Group
from student_groups.models import StudentGroup
import os, json

dir = os.path.dirname(__file__)


def load_test_data(output):
	Group.objects.create(name="students")
	Group.objects.create(name="registered")
	Group.objects.create(name="group admin")

	output.write("User groups were successfully created")

	# Groups creation
	groups = []
	with open(os.path.join(dir, 'json/groups.json')) as data_file:
		json_data = json.load(data_file)
		for data in json_data:
			groups.append(StudentGroup.objects.create(**data))

	output.write("Student groups were successfully created")
