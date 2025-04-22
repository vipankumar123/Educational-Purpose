

# views.py

from django.shortcuts import render
from .models import Book, Author
from django.http import HttpResponse


def book_list(request):
    books = Book.objects.select_related('author').all()
    data = []
    for i in books:
        data.append(i.author.name + "  ")
    return HttpResponse(data)


def author_list(request):
    authors = Author.objects.prefetch_related('book_set').all()
    books_by_author = {}
    for author in authors:
        book_titles = [book.title for book in author.book_set.all()]
        books_by_author[author.name] = book_titles
        for book_title in book_titles:
            print(f"{author.name}: {book_title}")
    response_text = '\n'.join([f"{author}: {', '.join(books)}" for author, books in books_by_author.items()])
    return HttpResponse(response_text)






























# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .serializers import ColorSerializer
# from django.http import HttpResponse

# from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
# from rest_framework.permissions import IsAuthenticated

# class FavoriteColorView(APIView):
#     def post(self, request):
#         serializer = ColorSerializer(data=request.data)
#         if serializer.is_valid():
#             color = serializer.validated_data['name']
#             request.session['favorite_color'] = color
#             return Response({'message': 'Favorite color set'}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def get(self, request):
#         favorite_color = request.session.get('favorite_color', None)
#         if favorite_color:
#             return Response({'favorite_color': favorite_color})
#         return Response({'message': 'Favorite color not set'}, status=status.HTTP_404_NOT_FOUND)

#     def delete(self, request):
#         if 'favorite_color' in request.session:
#             del request.session['favorite_color']
#             return Response({'message': 'Favorite color deleted'}, status=status.HTTP_204_NO_CONTENT)
#         return Response({'message': 'Favorite color not found'}, status=status.HTTP_404_NOT_FOUND)



# def set_cookie_data(request):
#     response = HttpResponse("cookie set!!")
#     response.set_cookie('favurite_color', 'Green', max_age=3600)
#     return response


# def get_cookie_data(request):
#     fav_colr = request.COOKIES.get('favurite_color', 'not set')
#     return HttpResponse('favourite color: ' + fav_colr)


# class MyViewAuth(APIView):
#     throttle_classes = [UserRateThrottle]  
#     permission_classes = [IsAuthenticated]  

#     def get(self, request, format=None):
#         # Your view logic here
#         return Response({'message': 'Hello, loggin user!'})

# class MyViewAnony(APIView):
#     throttle_classes = [AnonRateThrottle]  

#     def get(self, request, format=None):
#         # Your view logic here
#         return Response({'message': 'Hello, Anonymous user!'})