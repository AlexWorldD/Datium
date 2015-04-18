from django.contrib.auth.models import User
from rest_framework import generics, permissions
from users.serializers import UserSerializer
from student_groups.models import Student

# Create your views here.


class UserListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):

        group = self.request.QUERY_PARAMS.get('group', None)

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
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(self, request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(self, request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(self, request, *args, **kwargs)
