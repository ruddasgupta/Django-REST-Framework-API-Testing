from django.urls import path, reverse, include, resolve
from django.test import SimpleTestCase
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient

from ..views import ListCreateBookAPIView


class ApiUrlsTests(SimpleTestCase):

    def test_get_post_books_is_resolved(self):
        url = reverse('get_post_books')
        self.assertEquals(resolve(url).func.view_class, ListCreateBookAPIView)


class ListCreateBookAPIViewTests(APITestCase):
    books_url = reverse('get_post_books')

    def setUp(self):
        self.user = User.objects.create_user(
            username='username', password='p@ssw0rd1344')
        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_get_books_authenticated(self):
        response = self.client.get(self.books_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_books_un_authenticated(self):
        self.client.force_authenticate(user=None, token=None)
        response = self.client.get(self.books_url)
        self.assertEquals(response.status_code, 401)

    def test_post_books(self):
        data = {
            "title": "title",
            "description": "description",
            "publisher": "publisher",
            "author": "author",
            "year": 2023
        }
        response = self.client.post(self.books_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(response.data), 6)


class RetrieveUpdateDestroyBookAPIViewTests(APITestCase):
    books_url = reverse('get_post_books')
    book_url = reverse('get_delete_update_book', args=[1])

    def setUp(self):
        self.user = User.objects.create_user(
            username='username', password='p@ssw0rd1344')
        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        # Saving customer
        data = {
            "title": "title",
            "description": "description",
            "publisher": "publisher",
            "author": "author",
            "year": 2023
        }
        self.client.post(
            self.books_url, data, format='json')

    def test_get_book_autheticated(self):
        response = self.client.get(self.book_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], 'title')

    def test_get_book_un_authenticated(self):
        self.client.force_authenticate(user=None, token=None)
        response = self.client.get(self.book_url)
        self.assertEqual(response.status_code, 401)

    def test_delete_book_authenticated(self):
        response = self.client.delete(self.book_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
