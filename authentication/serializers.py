__author__ = 'Kirov'

from django.contrib.auth.models import User
from rest_framework import serializers
from student_groups.models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'user', 'group', 'avatar')

    def create(self, validated_data):
        return Student.objects.create(**validated_data)


class UserSerializer(serializers.ModelSerializer):
    student = StudentSerializer()

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'student')
        write_only_fields = ('password',)

    def create(self, validated_data):
        student_data = validated_data.pop('student')
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        Student.objects.create(user=user, **student_data)
        return user





