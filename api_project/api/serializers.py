from rest_framework import serializers
from .models import Book

# create a book class
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'