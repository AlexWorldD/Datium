from timetable.models import Subject
from rest_framework import generics
from timetable.serializers import SubjectSerializer

# Create your views here.


class SubjectListAPIView(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer