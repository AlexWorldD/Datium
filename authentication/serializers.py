__author__ = 'Kirov'

from django.contrib.auth.models import User
from rest_framework import serializers
from student_groups.models import Student, StudentGroup
from django.templatetags.static import static

class StudentSerializer(serializers.ModelSerializer):
    #user = UserSerializer()
    student_group = serializers.SlugRelatedField(slug_field = 'name')
    class Meta:
        model = Student
        #fields = ('user', 'student_group')
        fields = ('student_group')

    #def create(self, validated_data):
        #student = Student.objects.create(user = validated_data['user'], group = StudentGroup.objects.get(name = validated_data['student_group']), avatar = static('images/avatars/default_avatar.png'))
        #return student

class UserSerializer(serializers.ModelSerializer):
    student = StudentSerializer()
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        write_only_fields = ('password',)

    def create(self, validated_data):
        student_data = validated_data.pop('student')
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        st = Student.objects.create(user = user, group = StudentGroup.objects.get(name = student_data['student_group']), avatar = static('images/avatars/default_avatar.png'))
        st.save()
        return user