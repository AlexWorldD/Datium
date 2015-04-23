from django.contrib.auth.models import User
from rest_framework import generics, permissions
from users.serializers import UserSerializer
from student_groups.models import Student
from django.http import HttpResponse

from users.permissions import IsOwnerOrReadOnly

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
