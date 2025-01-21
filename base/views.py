from base.models import *
from account.models import *
from base.serializers import *
from django.http import Http404
from account.serializers import *
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class getUsers(APIView):
    """
    Retrieve a list of all users.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        try:
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
            message = {"detail": "Successfully retrieved all users."}
            return Response(
                {"data": serializer.data, "message": message},
                status=status.HTTP_200_OK
            )
        except Exception as e:
            message = {
                "detail": "An error occurred while retrieving users.",
                "error": str(e),
            }
            return Response({"message": message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class addUser(APIView):
    """
    Create a new user.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        try:
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                message = {"detail": "User created successfully."}
                return Response(
                    {"data": serializer.data, "message": message},
                    status=status.HTTP_201_CREATED
                )
            else:
                message = {
                    "detail": "Error creating user. Please check the fields.",
                    "errors": serializer.errors
                }
                return Response({"message": message}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            message = {
                "detail": "An unexpected error occurred while creating the user.",
                "error": str(e)
            }
            return Response({"message": message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
