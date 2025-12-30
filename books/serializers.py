
from rest_framework import serializers

from books.models import Book



class ListBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        exclude = ('added_by', 'created_at', 'updated_at')