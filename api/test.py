from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK, HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST,\
    HTTP_204_NO_CONTENT
from rest_framework.test import APIClient

from api.models import Message

User = get_user_model()

SAMPLE_MESSAGE = 'test message'
VIEWS_COUNT = 120


class MessageTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='message_user', password='secret_password')
        self.token = Token.objects.create(user=self.user)
        self.token.save()
        Message.objects.create(body=SAMPLE_MESSAGE, views=200)

    def test_message_list(self):
        client = APIClient()
        response = client.get(reverse('messages'))
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.json()[0]['body'], SAMPLE_MESSAGE)

    def test_message_get(self):
        client = APIClient()
        message = Message.objects.first()
        message.views = VIEWS_COUNT
        message.save()
        url = reverse('message', kwargs={'id': message.pk})
        response = client.get(url)
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(VIEWS_COUNT + 1, Message.objects.first().views)

    def test_new_message(self):
        client = APIClient()
        messages_before = Message.objects.all().count()
        response = client.post(reverse('messages'), data={
            'body': 'test'
        })
        self.assertEqual(response.status_code, HTTP_401_UNAUTHORIZED)
        self.assertEqual(messages_before, Message.objects.all().count())
        client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = client.post(reverse('messages'), data={
            'body': 'test'
        })
        self.assertEqual(response.status_code, HTTP_201_CREATED)
        self.assertEqual(messages_before + 1, Message.objects.all().count())

    def test_empty_message(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = client.post(reverse('messages'), data={
            'body': ''
        })
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)

    def test_too_long_message(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = client.post(reverse('messages'), data={
            'body': "x" * 161
        })
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)

    def test_update_message(self):
        updated_msg = 'updated message'
        client = APIClient()
        message = Message.objects.first()
        url = reverse('message', kwargs={'id': message.pk})
        response = client.put(url, data={
            'body': updated_msg
        })
        self.assertEqual(response.status_code, HTTP_401_UNAUTHORIZED)
        self.assertNotEqual(updated_msg, Message.objects.first().body)
        self.assertNotEqual(VIEWS_COUNT, Message.objects.first().views)
        client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = client.put(url, data={
            'body': updated_msg
        })
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(updated_msg, Message.objects.first().body)
        self.assertEqual(0, Message.objects.first().views)

    def test_update_message_empty(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        message = Message.objects.first()
        url = reverse('message', kwargs={'id': message.pk})
        response = client.put(url, data={
            'body': ''
        })
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)

    def test_update_message_too_long(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        message = Message.objects.first()
        url = reverse('message', kwargs={'id': message.pk})
        response = client.put(url, data={
            'body': 'x' * 161
        })
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)

    def test_delete_message(self):
        client = APIClient()
        message = Message.objects.first()
        messages_before = Message.objects.all().count()
        url = reverse('message', kwargs={'id': message.pk})
        response = client.delete(url)
        self.assertEqual(response.status_code, HTTP_401_UNAUTHORIZED)
        self.assertEqual(messages_before, Message.objects.all().count())
        client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = client.delete(url)
        self.assertEqual(response.status_code, HTTP_204_NO_CONTENT)
        self.assertEqual(messages_before - 1, Message.objects.all().count())
