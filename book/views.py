from rest_framework import viewsets

from book.models import Book
from book.serializers import BookSerializers


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializers
    queryset = Book.objects.all()
