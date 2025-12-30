from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status

from books.models import Book
from books.serializers import ListBookSerializer

# Create your views here.

class GetBooksView(ListAPIView):
    """
    Retrive all the books based on filters
    """
    queryset = Book.objects.all()
    serializer_class = ListBookSerializer


class AddBookAndReviewView:
    """
    Docstring for AddBookAndReviewView
    Users can submit a Book and Review but the submission will be under review
    after admin approval it will be published
    """

    pass

class AddReviewView:
    pass