
from rest_framework import serializers

from books.models import Book



class ListBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        exclude = ('added_by', 'created_at', 'updated_at')

class AddBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'author', 'title', 'description', 'language', 'image', 'added_by']
        read_only_fields = ['added_by']

class BookReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'