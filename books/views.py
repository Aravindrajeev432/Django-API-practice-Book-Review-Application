from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser



from books.models import Book
from books.serializers import AddBookSerializer, ListBookSerializer

# Create your views here.

class GetBooksView(generics.ListAPIView):
    """
    Retrive all the books based on filters
    """
    queryset = Book.objects.all()
    serializer_class = ListBookSerializer

class AddBookView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]
    @swagger_auto_schema(
            operation_description="Upload a new book with an image cover.",
            operation_summary="Create Book",
            request_body=AddBookSerializer,
            responses={
                201: AddBookSerializer,
                400: "Bad Request - Validation Errors",
                401: "Unauthorized - Authentication Required"
            },
            tags=['Books']
        )
    def post(self, request):
        #check if book already exist
        serializer = AddBookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(added_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        if serializer.errors:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    


class AddBookAndReviewView:
    """
    Docstring for AddBookAndReviewView
    Users can submit a Book and Review but the submission will be under review
    after admin approval it will be published
    """

    pass

class AddReviewView:
    pass