__author__ = 'Kirov'

from timetable.models import Subject, Teacher, Department, Lesson, LessonInTimeTable
from rest_framework import serializers
from student_groups.models import StudentGroup
from django.utils import timezone


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('id', 'name')

    def create(self, validated_data):
        return Subject.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('id', 'name')

    def create(self, validated_data):
        return Department.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = ('id', 'first_name', 'last_name', 'patronymic', 'email', 'phone', 'cabinet')

    def create(self, validated_data):
        return Teacher.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.patronymic = validated_data.get('patronymic', instance.patronymic)
        instance.email = validated_data.get('email', instance.email)
        instance.phone = validated_data.get('phone', instance.email)
        instance.cabinet = validated_data.get('cabinet', instance.cabinet)
        instance.save()
        return instance

class LessonSerializer(serializers.ModelSerializer):

    subject = serializers.SlugRelatedField(slug_field='name', queryset=Subject.objects.all())
    teacher = serializers.PrimaryKeyRelatedField(queryset=Teacher.objects.all())
    group = serializers.SlugRelatedField(queryset=StudentGroup.objects.all(), slug_field='name')
    lesson_type = serializers.ChoiceField(choices=Lesson.LESSON_TYPE_CHOICES)
    day = serializers.ChoiceField(choices=Lesson.WEEKDAY)

    class Meta:
        model = Lesson
        fields = ('subject', 'teacher', 'group', 'semester', 'lesson_type', 'day', 'class_number')

    def create(self, validated_data):
        return Lesson.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.subject = validated_data.get('subject', instance.subject)
        instance.teacher = validated_data.get('teacher', instance.teacher)
        instance.semester = validated_data.get('semester', instance.semester)
        instance.lesson_type = validated_data.get('lesson_type', instance.lesson_type)
        instance.day = validated_data.get('day', instance.day)
        instance.class_number = validated_data.get('class_number', instance.class_number)

        instance.save()
        return instance

class DateTimeTzAwareField(serializers.DateTimeField):
    def to_representation(self, value):
        value = timezone.localtime(value)
        return super(DateTimeTzAwareField, self).to_representation(value)

class LessonInTimetableSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer(read_only=True)
    date = serializers.DateField(source='day.date')
    start = DateTimeTzAwareField()
    end = DateTimeTzAwareField()

    class Meta:
        model = LessonInTimeTable
        fields = ('id', 'lesson', 'start', 'end', 'date')
