from timetable.models import Subject, Teacher, Lesson
from rest_framework import generics, permissions
from timetable.serializers import SubjectSerializer, TeacherSerializer, LessonSerializer
from users.permissions import CanViewTimetable, CanAddAndEditSubjects, CanAddAndEditTeachers, CanEditTimetable
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class SubjectListAPIView(generics.ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return [permissions.IsAuthenticated(), CanViewTimetable(),]
        return [permissions.IsAuthenticated(), CanAddAndEditSubjects(),]


class SubjectDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(self, request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(self, request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(self, request, *args, **kwargs)

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return [permissions.IsAuthenticated(), CanViewTimetable(),]
        return [permissions.IsAuthenticated(), CanAddAndEditSubjects(),]


class TeacherListAPIView(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return [permissions.IsAuthenticated(), CanViewTimetable(),]
        return [permissions.IsAuthenticated(), CanAddAndEditTeachers()]


class TeacherDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(self, request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(self, request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(self, request, *args, **kwargs)

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return [permissions.IsAuthenticated(), CanViewTimetable(),]
        return [permissions.IsAuthenticated(), CanAddAndEditTeachers(),]

class LessonListCreateAPIView(generics.ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return [permissions.IsAuthenticated(), CanViewTimetable(),]
        return [permissions.IsAuthenticated(), CanEditTimetable(),]

    def post(self, request, *args, **kwargs):
        data = request.data.copy()
        data['group'] = request.user.student.group.name
        try:
            Subject.objects.get(name = data['subject'])
        except Subject.DoesNotExist:
            Subject.objects.create(name = data['subject'])
        serializer = LessonSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LessonDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return [permissions.IsAuthenticated(), CanViewTimetable(),]
        return [permissions.IsAuthenticated(), CanEditTimetable(),]