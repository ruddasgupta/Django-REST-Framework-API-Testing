import unittest
from ..serializers import BookSerializer
from ..models import Book


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.book_attributes = {
            "title": "title",
            "description": "description",
            "publisher": "publisher",
            "author": "author",
            "year": 2023
        }

        self.serializer_data = {
            "title": "title",
            "description": "description",
            "publisher": "publisher",
            "author": "author",
            "year": 2023
        }

        self.book = Book.objects.create(**self.book_attributes)
        self.serializer = BookSerializer(instance=self.book)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), {'id', 'title', 'description', 'publisher', 'author', 'year'})

    def test_title_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['title'], self.book_attributes['title'])

    def test_year_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['year'], self.book_attributes['year'])

    def test_year_upper_bound(self):
        self.serializer_data['year'] = 2025
        serializer = BookSerializer(data=self.serializer_data)
        self.assertFalse(serializer.is_valid())
        self.assertEqual(set(serializer.errors), {'year'})

    def test_year_lower_bound(self):
        self.serializer_data['year'] = -1
        serializer = BookSerializer(data=self.serializer_data)
        self.assertFalse(serializer.is_valid())
        self.assertEqual(set(serializer.errors), {'year'})
