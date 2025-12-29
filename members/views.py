from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import RegistrationSerializer

class RegistrationView(APIView):
    """
    Docstring for RegistrationView

    """
    # Required for image uploads
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
        print("POST")
        print(f"request.data: {request.data}") # print the request.data)
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "User created successfully"}, 
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)