from account.models import *
from django.http import Http404
from account.serializers import *
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

class getUsers(APIView):
    """
    Retrieve a list of all users.
    """
    def get(self, request, format=None):
        try:
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
            message = {"detail": "Successfully retrieved all users."}
            return Response({"data": serializer.data, "message": message}, status=status.HTTP_200_OK)
        except Exception as e:
            message = {
                "detail": "An error occurred while retrieving users.",
                "error": str(e)
            }
            return Response({"message": message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class addUser(APIView):
    """
    Create a new user.
    """
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            message = {"detail": "User created successfully."}
            return Response({"data": serializer.data, "message": message}, status=status.HTTP_201_CREATED)
        else:
            # Serializer errors include details per field
            message = {
                "detail": "Error creating user. Please check the fields.",
                "errors": serializer.errors
            }
            return Response({"message": message}, status=status.HTTP_400_BAD_REQUEST)
