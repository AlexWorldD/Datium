from student_groups.models import Student, StudentGroup, Document
from student_groups.serializers import StudentGroupSerializer, DocumentSerializer
from rest_framework import generics, permissions
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
import shutil

# Create your views here.


class StudentGroupListAPIView(generics.ListAPIView):
    queryset = StudentGroup.objects.all()
    serializer_class = StudentGroupSerializer
    permission_classes = (permissions.AllowAny,)


class StudentGroupDetailAPIView(generics.RetrieveAPIView):
    queryset = StudentGroup.objects.all()
    serializer_class = StudentGroupSerializer
    
class DocumentCreateAPIView(generics.CreateAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    parser_classes = (FormParser, MultiPartParser,)
    def post(self, request, *args, **kwargs):
        data = request.DATA
        data['group'] = request.user.student.group.name
        data['file'] = request.FILES['file']
        serializer = DocumentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            serializer_data = serializer.data
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DocumentListAPIView(generics.ListAPIView):
    serializer_class = DocumentSerializer
    def get_queryset(self):
        return Document.objects.filter(group = self.request.user.student.group)

class DocumentDetailAPIView(generics.RetrieveAPIView):
    serializer_class = DocumentSerializer
    def get_queryset(self):
        return Document.objects.filter(group = self.request.user.student.group)