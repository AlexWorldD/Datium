from student_groups.models import StudentGroup, Tag, Document, News
from comments.models import CommentsTable
from rest_framework import serializers
from comments.serializers import CommentsTableObjectRelatedField
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User


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
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    group = serializers.SlugRelatedField(queryset = StudentGroup.objects.all(), slug_field = 'name')
    tags = TagField(allow_null=True, queryset=Tag.objects.all(), required=False)
    comments = CommentsTableObjectRelatedField(read_only = True)
    
    class Meta:
        model = Document
        fields = ('id', 'file', 'name', 'user', 'group', 'tags', 'comments')

    def create(self, validated_data):
        tags_data = validated_data.pop('tags', None)
        document = Document.objects.create(**validated_data)
        if tags_data != None:
            document.tags.add(*tags_data)
        CommentsTable.objects.create(content_object = document)
        document.save()
        return document

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.tags = validated_data.get('tags', instance.tags.all())
        instance.save()
        return instance


class NewsSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    group = serializers.SlugRelatedField(queryset=StudentGroup.objects.all(), slug_field='name')
    tags = TagField(allow_null=True, queryset=Tag.objects.all(), required=False)
    comments = CommentsTableObjectRelatedField(read_only = True)
    documents = serializers.PrimaryKeyRelatedField(many = True, required=False, queryset=Document.objects.all())

    class Meta:
        model = News
        fields = ('id', 'title', 'text', 'pub_date', 'user', 'group', 'tags', 'comments', 'documents')

    def create(self, validated_data):
        tags_data = validated_data.pop('tags', None)
        group = validated_data.get('group')
        documents = validated_data.pop('documents', None)
        if documents != None:
            for document in documents:
                if document.group != group:
                    validated_data['documents'].remove(document)
        news = News.objects.create(**validated_data)
        if tags_data != None:
            news.tags.add(*tags_data)
        if documents != None:
            news.documents.add(*documents)
        CommentsTable.objects.create(content_object = news)
        news.save()
        return news

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.text = validated_data.get('text', instance.text)
        instance.pub_date = validated_data.get('pub_date', instance.pub_date)
        instance.tags = validated_data.get('tags', instance.tags.all())
        instance.documents = validated_data.get('documents', instance.documents.all())
        instance.save()
        return instance