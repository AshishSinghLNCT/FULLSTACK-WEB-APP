from django.shortcuts import render
from rest_framework import viewsets
from .models import User, Interest, ChatMessage
from .serializers import UserSerializer, InterestSerializer, ChatMessageSerializer
from rest_framework.permissions import IsAuthenticated

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class InterestViewSet(viewsets.ModelViewSet):
    queryset = Interest.objects.all()
    serializer_class = InterestSerializer
    permission_classes = [IsAuthenticated]

class ChatMessageViewSet(viewsets.ModelViewSet):
    queryset = ChatMessage.objects.all()
    serializer_class = ChatMessageSerializer
    permission_classes = [IsAuthenticated]

