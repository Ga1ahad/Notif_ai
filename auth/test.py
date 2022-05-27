from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK

User = get_user_model()

USERNAME_01 = 'test01'
USERNAME_02 = 'test02'
PASSWORD = 'Test1234!'
WRONG_PASSWORD = 'Test'
AUTH_URL = 'http://127.0.0.1:8000/auth'


class UserTest(TestCase):

    def setUp(self):
        User.objects.create_user(username=USERNAME_01, password=PASSWORD)

    def test_register_user_with_blank_password(self):
        url = reverse('register')
        clients_before = User.objects.all().count()
        response = self.client.post(url, data={
            'username': USERNAME_01,
            'password': '',
        })
        clients_after = User.objects.all().count()
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEquals(clients_before, clients_after)

    def test_register_user_with_existing_username(self):
        url = reverse('register')
        clients_before = User.objects.all().count()
        response = self.client.post(url, data={
            'username': USERNAME_01,
            'password': PASSWORD,
        })
        clients_after = User.objects.all().count()
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEquals(clients_before, clients_after)

    def test_register_user(self):
        url = reverse('register')
        response = self.client.post(url, data={
            'username': USERNAME_02,
            'password': PASSWORD,
        })
        self.assertEqual(response.status_code, HTTP_201_CREATED)
        self.assertIsNotNone(User.objects.get(username=USERNAME_02))

    def test_wrong_credentials(self):
        url = reverse('token')
        response = self.client.post(url, data={
            'username': USERNAME_01,
            'password': WRONG_PASSWORD,
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login(self):
        url = reverse('token')
        response = self.client.post(url, data={
            'username': USERNAME_01,
            'password': PASSWORD,
        })
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertIn('token', response.json())
