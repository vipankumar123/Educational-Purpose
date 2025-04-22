# urls.py
from django.urls import path
from .views import create_book, get_books

urlpatterns = [
    path('api/create_book/', create_book, name='create_book'),
    path('api/books/', get_books, name='get_books'),
]
