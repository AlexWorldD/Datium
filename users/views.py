from django.contrib.auth.models import User
from rest_framework import generics, permissions
from users.serializers import UserSerializer
from student_groups.models import Student
from django.http import HttpResponse
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
from django.core.files import File
from django.conf import settings

from users.permissions import IsOwnerOrReadOnly, IsOwner

# Create your views here.

class UserListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):

        group = self.request.user.student.group

        try:
            students = Student.objects.filter(group=group)
        except Student.DoesNotExist:
            students = None

        queryset = []
        for student in students:
            if student.user is not None:
                queryset.append(student.user)
        return queryset

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return permissions.IsAuthenticated(),
        return permissions.AllowAny(),


class UserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly,)
    lookup_field = 'username'
    
class UserDetailByIDAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly,)

class UserAvatarUploadAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (permissions.IsAuthenticated, IsOwner,)
    parser_classes = (FormParser, MultiPartParser,)
    lookup_field = 'username'
    def post(self, request, *args, **kwargs):
        user = request.user
        given_file = request.FILES.get('file', request.user.student.avatar)
        print(settings.MEDIA_ROOT)
        print(given_file.name)
        user.student.avatar.save(name = given_file.name, content = File(given_file))
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class UserAvatarUploadByIDAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (permissions.IsAuthenticated, IsOwner,)
    parser_classes = (FormParser, MultiPartParser,)
    def post(self, request, *args, **kwargs):
        user = request.user
        user.student.avatar = request.FILES.get('file', request.user.student.avatar)
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)