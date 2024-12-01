from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase

class BookAPITests(APITestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        # Create test data (e.g., a book object)
        self.author = Author.objects.create(name="Test Author")
        self.book_data = {
            "title": "Test Book",
            "publication_year": 2020,
            "author": self.author.id,
        }

    def test_create_book_authenticated(self):
        # Log in the user
        self.client.login(username='testuser', password='testpassword')
        
        # Send the request with authenticated user
        response = self.client.post('/api/books/', self.book_data, format='json')

        # Assert that the request was successful (status 201)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_book_unauthenticated(self):
        # Send the request without logging in (should fail)
        response = self.client.post('/api/books/', self.book_data, format='json')

        # Assert that the request fails with status 401 (unauthorized)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
