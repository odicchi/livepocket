from django.contrib.auth.models import User
from rest_framework import generics, permissions

from .models import Ticket
from .serializers import UserSerializer, TicketSerializer

class UserList(generics.ListAPIView):
    """ View to list all users"""
    queryset = User.objects.all().order_by('first_name')
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated, )

class UserCreate(generics.CreateAPIView):
    """ View to create a new user. Only accepts POST requests """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAdminUser, )

class UserRetrieveUpdate(generics.CreateAPIView):
    """ Retrieve a user or update user information.
    Accepts GET and PUT requests and the record id must be provided in the request """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated, )

class TicketCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = TicketSerializer
    permission_classes = (permissions.IsAuthenticated, )

