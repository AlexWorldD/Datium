from django.contrib.auth.models import User
from rest_framework import generics
from authentication.serializers import UserSerializer


# Create your views here.


class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer