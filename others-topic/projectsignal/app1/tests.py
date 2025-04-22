from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book


class BootAPITests(APITestCase):

    def test_create_book(self):
        url = reverse('create_book')
        data = {'title': "Test Book", 'author': "Test Author", 'published_date': "2024-3-25"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 1)
        self.assertEqual(Book.objects.get().title, 'Test Book')

    def test_get_books(self):

        Book.objects.create(title="Test Book1", author="Test Author1", published_date="2024-3-25")
        Book.objects.create(title="Test Book2", author="Test Author2", published_date="2024-3-25")

        url = reverse('get_books')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)




    