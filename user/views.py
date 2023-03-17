from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from rest_framework import viewsets

from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer

  def perform_create(self, serializer):
    serializer.save(password=make_password(serializer.validated_data['password'])),