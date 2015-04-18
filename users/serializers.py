__author__ = 'Kirov'

from django.contrib.auth.models import User, Group
from rest_framework import serializers
from student_groups.models import Student, StudentGroup
from django.templatetags.static import static


class UserSerializer(serializers.ModelSerializer):
    group = serializers.SlugRelatedField(source='student.group', queryset=StudentGroup.objects.all(), slug_field='name')
    avatar = serializers.ImageField(source='student.avatar', default=static('images/avatars/default_avatar.png'))
    sex = serializers.CharField(source='student.sex', default='unknown')

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'group', 'sex', 'avatar', 'first_name', 'last_name')
        write_only_fields = ('password',)

    def create(self, validated_data):
        student_data = validated_data.pop('student')
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.groups.add(Group.objects.get(name='registered'))
        user.save()
        Student.objects.create(user=user, group=student_data['group'])
        return user

    def update(self, instance, validated_data):
        student_data = validated_data.pop('student')
        student = instance.student
        student.sex = student_data.get('sex', student.sex)
        student.avatar = student_data.get('avatar', student.avatar)
        student.save()
        instance.save()
        return instance
