from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from .models import Interest, ChatMessage

User = get_user_model()

class UserTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')

    def test_create_user(self):
        url = reverse('user-list')
        data = {'username': 'newuser', 'password': 'newpassword'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_user(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('user-detail', args=[self.user.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], self.user.username)

class InterestTests(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='user1', password='password123')
        self.user2 = User.objects.create_user(username='user2', password='password123')
        self.client.force_authenticate(user=self.user1)

    def test_create_interest(self):
        url = reverse('interest-list')
        data = {'sender': self.user1.id, 'receiver': self.user2.id, 'message': 'Hello!'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_interest(self):
        interest = Interest.objects.create(sender=self.user1, receiver=self.user2, message='Hello!')
        url = reverse('interest-detail', args=[interest.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], interest.message)

class ChatMessageTests(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='user1', password='password123')
        self.user2 = User.objects.create_user(username='user2', password='password123')
        self.client.force_authenticate(user=self.user1)

    def test_create_chat_message(self):
        url = reverse('chatmessage-list')
        data = {'sender': self.user1.id, 'receiver': self.user2.id, 'message': 'Hi there!'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_chat_message(self):
        chat_message = ChatMessage.objects.create(sender=self.user1, receiver=self.user2, message='Hi there!')
        url = reverse('chatmessage-detail', args=[chat_message.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], chat_message.message)

