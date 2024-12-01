from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book, Author

class BookAPITests(APITestCase):

    def setUp(self):
        self.author = Author.objects.create(name="Author Test")
        self.book_data = {
            "title": "Test Book",
            "publication_year": 2020,
            "author": self.author.id,
        }

    def test_create_book(self):
        response = self.client.post('/api/books/', self.book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_book(self):
        book = Book.objects.create(**self.book_data)
        updated_data = {"title": "Updated Book"}
        response = self.client.put(f'/api/books/{book.id}/', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
