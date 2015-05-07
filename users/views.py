from django.contrib.auth.models import User, Group
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

from users.permissions import IsUserOrReadOnly, IsUser, CanViewGrouplist, CanChangePermissions, IsUserOrCanDeleteUsers

# Create your views here.

class UserListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(student__group = self.request.user.student.group)


    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return [permissions.IsAuthenticated(), CanViewGrouplist(),]
        return [permissions.AllowAny(),]


class UserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    lookup_field = 'username'
    def get_permissions(self):
        if self.request.method == "DELETE":
            return [permissions.IsAuthenticated(), IsUserOrCanDeleteUsers(),]
        return [permissions.IsAuthenticated(), IsUserOrReadOnly(),]

    def get_queryset(self):
        return User.objects.filter(student__group = self.request.user.student.group)

    
class UserDetailByIDAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.request.method == "DELETE":
            return [permissions.IsAuthenticated(), IsUserOrCanDeleteUsers(),]
        return [permissions.IsAuthenticated(), IsUserOrReadOnly(),]

    def get_queryset(self):
        return User.objects.filter(student__group=self.request.user.student.group)


class UserAvatarUploadAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (permissions.IsAuthenticated, IsUser,)
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
    permission_classes = (permissions.IsAuthenticated, IsUser,)
    parser_classes = (FormParser, MultiPartParser,)
    def post(self, request, *args, **kwargs):
        user = request.user
        user.student.avatar = request.FILES.get('file', request.user.student.avatar)
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ChangeUserPermissionsAPIView(generics.UpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated, CanChangePermissions,)
    lookup_field = 'username'
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

    def patch(self, request, *args, **kwargs):
        changed_user = self.get_object()
        group = request.data.get('group', None)
        if group == 'registered':
            changed_user.groups.clear()
            changed_user.groups.add(Group.objects.get(name = 'registered'))
        elif group == 'students':
            changed_user.groups.clear()
            changed_user.groups.add(Group.objects.get(name = 'registered'), Group.objects.get(name = 'students'))
        elif group == 'group admin':
            return Response("Can't assign new admin to a group yet", status = status.HTTP_400_BAD_REQUEST)
        else:
            return Response("No group provided", status = status.HTTP_400_BAD_REQUEST)
        changed_user.save()
        serializer = UserSerializer(changed_user)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    def put(self, request, *args, **kwargs):
        return Response('Please use patch method instead put', status=status.HTTP_400_BAD_REQUEST)


class ChangeUserPermissionsByIDAPIView(generics.UpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated, CanChangePermissions,)
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

    def patch(self, request, *args, **kwargs):
        changed_user = self.get_object()
        group = request.data.get('group', None)
        if group == 'registered':
            changed_user.groups.clear()
            changed_user.groups.add(Group.objects.get(name = 'registered'))
        elif group == 'students':
            changed_user.groups.clear()
            changed_user.groups.add(Group.objects.get(name = 'registered'), Group.objects.get(name = 'students'))
        elif group == 'group admin':
            return Response("Can't assign new admin to a group yet", status = status.HTTP_400_BAD_REQUEST)
        else:
            return Response("No group provided", status = status.HTTP_400_BAD_REQUEST)
        changed_user.save()
        serializer = UserSerializer(changed_user)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    def put(self, request, *args, **kwargs):
        return Response('Please use patch method instead put', status=status.HTTP_400_BAD_REQUEST)