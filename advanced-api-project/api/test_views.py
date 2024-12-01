class BookAPITests(APITestCase):
    def setUp(self):
        self.author = Author.objects.create(name="Test Author")
        self.book_data = {
            "title": "Test Book",
            "publication_year": 2020,
            "author": self.author.id,
        }

    def test_create_book(self):
        response = self.client.post('/api/books/', self.book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], self.book_data['title'])
        self.assertEqual(response.data['publication_year'], self.book_data['publication_year'])
        self.assertEqual(response.data['author'], self.author.id)

    def test_list_books(self):
        response = self.client.get('/api/books/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) > 0)  # Check if there is at least one book in the list
