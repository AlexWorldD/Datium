from student_groups.models import Student, StudentGroup, Document
from student_groups.serializers import StudentGroupSerializer, DocumentSerializer
from rest_framework import generics, permissions

# Create your views here.


class StudentGroupListAPIView(generics.ListAPIView):
    queryset = StudentGroup.objects.all()
    serializer_class = StudentGroupSerializer
    permission_classes = (permissions.AllowAny,)


class StudentGroupDetailAPIView(generics.RetrieveAPIView):
    queryset = StudentGroup.objects.all()
    serializer_class = StudentGroupSerializer
    
class DocumentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    