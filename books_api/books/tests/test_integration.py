import unittest
import requests


class TestAPI(unittest.TestCase):
    URL = 'http://127.0.0.1:8080/api/v1/'
    TOKEN = ''

    def setUp(self):
        res = requests.post(self.URL + 'auth/token/', json={
            "username": "username",
            "password": "p@ssw0rd1344"
        })
        self.TOKEN = res.json()['access']

    def test_get_books(self):
        url = self.URL + "books"
        token = 'Bearer ' + self.TOKEN
        payload = {}
        headers = {
            'Authorization': token}
        response = requests.request("GET", url, headers=headers, data=payload)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(type(response.json()['count']), type(0))

    def test_post_book(self):
        url = self.URL + "books/"
        token = 'Bearer ' + self.TOKEN
        payload = {
            "title": "title",
            "description": "description",
            "publisher": "publisher",
            "author": "author",
            "year": 2023
        }
        headers = {
            'Authorization': token}
        response = requests.request("POST", url, headers=headers, data=payload)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['title'], 'title')
        self.assertEqual(response.json()['description'], 'description')
        self.assertEqual(response.json()['publisher'], 'publisher')
        self.assertEqual(response.json()['author'], 'author')
        self.assertEqual(response.json()['year'], 2023)

    def test_get_book(self):
        url = self.URL + "books/1"
        token = 'Bearer ' + self.TOKEN
        payload = {}
        headers = {
            'Authorization': token}
        response = requests.request("GET", url, headers=headers, data=payload)
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.json()['title'])
        self.assertIsNotNone(response.json()['description'])
        self.assertIsNotNone(response.json()['publisher'])
        self.assertIsNotNone(response.json()['author'])
        self.assertIsNotNone(response.json()['year'])