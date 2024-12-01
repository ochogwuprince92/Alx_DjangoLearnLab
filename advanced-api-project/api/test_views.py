from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from api.models import Author, Book

class BookAPITests(APITestCase):

    def setUp(self):
        # Create test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

        # Create author for books
        self.author = Author.objects.create(name="Test Author")
        self.book_data = {
            "title": "Test Book",
            "publication_year": 2020,
            "author": self.author.id,
        }

    def test_create_book(self):
        # Send a POST request to create a book
        response = self.client.post('/api/books/', self.book_data, format='json')

        # Check if the status code is 201 (created)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Check the response data
        self.assertIn("id", response.data)  # Verify that the response includes an 'id'
        self.assertEqual(response.data["title"], "Test Book")
        self.assertEqual(response.data["author"], self.author.id)
        self.assertEqual(response.data["publication_year"], 2020)

    def test_list_books(self):
        # Create a book directly in the database
        book = Book.objects.create(title="Test Book", publication_year=2020, author=self.author)

        # Send a GET request to retrieve the list of books
        response = self.client.get('/api/books/', format='json')

        # Check if the status code is 200 (OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check the response data
        self.assertEqual(len(response.data), 1)  # Ensure only one book is returned
        self.assertEqual(response.data[0]["title"], "Test Book")
        self.assertEqual(response.data[0]["author"], self.author.id)
        self.assertEqual(response.data[0]["publication_year"], 2020)
