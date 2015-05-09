from student_groups.models import Student, StudentGroup, Document, News
from student_groups.serializers import StudentGroupSerializer, DocumentSerializer, NewsSerializer
from rest_framework import generics, permissions
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser
from rest_framework.response import Response
from rest_framework import status
from users.permissions import CanAddAndEditDocuments, CanViewDocuments, IsOwnerOrAdmin, CanViewNews, CanAddAndEditNews
import datetime

# Create your views here.


class StudentGroupListAPIView(generics.ListAPIView):
    queryset = StudentGroup.objects.all()
    serializer_class = StudentGroupSerializer
    permission_classes = (permissions.AllowAny,)


class StudentGroupDetailAPIView(generics.RetrieveAPIView):
    queryset = StudentGroup.objects.all()
    serializer_class = StudentGroupSerializer


class DocumentListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = DocumentSerializer
    parser_classes = (FormParser, MultiPartParser,)
    def post(self, request, *args, **kwargs):
        data = request.DATA
        data['user'] = request.user.id
        data['group'] = request.user.student.group.name
        data['file'] = request.FILES['file']
        serializer = DocumentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def get_queryset(self):
        return Document.objects.filter(group = self.request.user.student.group)
    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return [permissions.IsAuthenticated(), CanViewDocuments()]
        return [permissions.IsAuthenticated(), CanAddAndEditDocuments()]


class DocumentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DocumentSerializer
    def get_queryset(self):
        return Document.objects.filter(group = self.request.user.student.group)
    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return [permissions.IsAuthenticated(), CanViewDocuments(),]
        return [permissions.IsAuthenticated(), CanAddAndEditDocuments(), IsOwnerOrAdmin()]
    def delete(self, request, *args, **kwargs):
        comments_table = self.get_object().comments.objects.all()[0]
        comments = comments_table.comments.all()
        for each in comments:
            each.delete()
        comments_table.delete()
        return self.destroy(self, request, *args, **kwargs)


class NewsListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = NewsSerializer
    parser_classes = (JSONParser,)

    def post(self, request, *args, **kwargs):
        data = request.data.copy()
        data['user'] = request.user.id
        data['group'] = request.user.student.group.name
        serializer = NewsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        return News.objects.filter(group = self.request.user.student.group)

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return [permissions.IsAuthenticated(), CanViewNews(),]
        return [permissions.IsAuthenticated(), CanAddAndEditNews(),]


class NewsRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NewsSerializer
    def get_queryset(self):
        return News.objects.filter(group = self.request.user.student.group)
    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return [permissions.IsAuthenticated(), CanViewNews(),]
        return [permissions.IsAuthenticated(), CanAddAndEditNews(), IsOwnerOrAdmin()]
    def delete(self, request, *args, **kwargs):
        comments_table = self.get_object().comments.objects.all()[0]
        comments = comments_table.comments.all()
        for each in comments:
            each.delete()
        comments_table.delete()
        return self.destroy(self, request, *args, **kwargs)