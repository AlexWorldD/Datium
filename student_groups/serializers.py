from student_groups.models import StudentGroup, Tag, Document
from comments.models import CommentsTable
from rest_framework import serializers
from comments.serializers import CommentsTableObjectRelatedField
from django.core.exceptions import ObjectDoesNotExist


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


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name')

    def create(self, validated_data):
        return Tag.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

class TagField(serializers.RelatedField):
    def to_representation(self, value):
        result = ''
        for tag in value.all():
            result += tag.name + ';'
        return result
    def to_internal_value(self, data):
        tags_names_list = data.split(';')
        tags_names_list = filter(bool, tags_names_list) #delete empty strings
        tags = []
        for tag_name in tags_names_list:
            obj, created = Tag.objects.get_or_create(name = tag_name)
            tags.append(obj)
        return tags

class DocumentSerializer(serializers.ModelSerializer):
    file = serializers.FileField()
    group = serializers.SlugRelatedField(queryset = StudentGroup.objects.all(), slug_field = 'name')
    tags = TagField(allow_null=True, queryset=Tag.objects.all(), required=False)
    comments = CommentsTableObjectRelatedField(read_only = True)
    
    class Meta:
        model = Document
        fields = ('id', 'file', 'name', 'group', 'tags', 'comments')
    def create(self, validated_data):
        tags_data = validated_data.pop('tags', None)
        document = Document.objects.create(**validated_data)
        if tags_data != None:
            document.tags.add(*tags_data)
        comments = CommentsTable.objects.create(content_object = document)
        document.save()
        return document
