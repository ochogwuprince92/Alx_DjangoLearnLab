from rest_framework import serializers
from .models import Book, Author
import datetime

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__' # Serialize all fields of the Book model

# valdate that the publication year is not in the future
def validate_publication_year(self, value):
    current_year = datetime.datetime.now().year
    if value > current_year:
        raise serializers.ValidationError(f"Publication year cannot be in the future. Current year is {current_year}.")
    return value

# create Author serializer with nested BookSerializer
class AuthorSerializer(serializers.ModelSerializer):
    name = serializers.CharField() #Specify that the 'name' field should be serialized as a CharField
    books = BookSerializer(many=all, read_only=True) # Nested serializer for related books

# create a meta class for the AuthorSerializer    
    class Meta:
        model = Author
        fields = ['name', 'books']  # Include name and related books in the serialized output
