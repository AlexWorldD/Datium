from student_groups.models import StudentGroup
from rest_framework import serializers


class StudentGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentGroup
        fields = ('id', 'name', 'study_year',)

    def create(self, validated_data):
        return StudentGroup.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.study_year = validated_data.get('study_year', instance.study_year)
        instance.save()
        return instance
