__author__ = 'Kirov'

from django.contrib.auth.models import User, Group
from rest_framework import serializers
from student_groups.models import Student, StudentGroup
from django.templatetags.static import static


class UserSerializer(serializers.ModelSerializer):
    group = serializers.SlugRelatedField(source='student.group', queryset=StudentGroup.objects.all(), slug_field='name')
    avatar = serializers.ImageField(source='student.avatar', default=static('images/avatars/default_avatar.png'))
    sex = serializers.CharField(source='student.sex', default='unknown')
    phone = serializers.CharField(source='student.phone', default='empty', allow_blank=True)
    city = serializers.CharField(source='student.city', default='empty', allow_blank=True)
    hall = serializers.CharField(source='student.hall', default='empty', allow_blank=True)
    permissions = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'group', 'sex', 'avatar',
                  'first_name', 'last_name', 'phone', 'city', 'hall', 'permissions')
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
        if 'student' in validated_data:
            student_data = validated_data.pop('student')
            student = instance.student
            student.sex = student_data.get('sex', student.sex)
            student.avatar = student_data.get('avatar', student.avatar)
            student.city = student_data.get('city', student.city)
            student.hall = student_data.get('hall', student.hall)
            student.phone = student_data.get('phone', student.phone)
            student.save()
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.save()
        return instance

    def get_permissions(self, obj):
        group1 = Group.objects.get(name = 'registered')
        group2 = Group.objects.get(name = 'students')
        group3 = Group.objects.get(name = 'group admin')
        if group3 in obj.groups.all():
            return 'group admin'
        if group2 in obj.groups.all():
            return 'students'
        if group1 in obj.groups.all():
            return 'registered'
        return 'undefined'
