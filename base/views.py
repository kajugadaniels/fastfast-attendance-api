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

class showUser(APIView):
    """
    Retrieve detailed information about a specific user.
    """
    def get_object(self, id):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
            raise Http404(f"User with id {id} does not exist.")

    def get(self, request, id, format=None):
        try:
            user = self.get_object(id)
            serializer = UserSerializer(user)
            message = {"detail": "User retrieved successfully."}
            return Response({"data": serializer.data, "message": message}, status=status.HTTP_200_OK)
        except Http404 as e:
            message = {"detail": str(e)}
            return Response({"message": message}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            message = {"detail": "An error occurred while retrieving the user.", "error": str(e)}
            return Response({"message": message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class editUser(APIView):
    """
    Update an existing user completely (PUT) or partially (PATCH).
    """
    def get_object(self, id):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
            raise Http404(f"User with id {id} does not exist.")

    def put(self, request, id, format=None):
        """
        Handle complete update of a user.
        """
        try:
            user = self.get_object(id)
            serializer = UserSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                message = {"detail": "User updated successfully."}
                return Response({"data": serializer.data, "message": message}, status=status.HTTP_200_OK)
            else:
                message = {
                    "detail": "Error updating user. Please check the fields.",
                    "errors": serializer.errors
                }
                return Response({"message": message}, status=status.HTTP_400_BAD_REQUEST)
        except Http404 as e:
            message = {"detail": str(e)}
            return Response({"message": message}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            message = {"detail": "An error occurred while updating the user.", "error": str(e)}
            return Response({"message": message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def patch(self, request, id, format=None):
        """
        Handle partial update of a user.
        """
        try:
            user = self.get_object(id)
            serializer = UserSerializer(user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                message = {"detail": "User updated successfully."}
                return Response({"data": serializer.data, "message": message}, status=status.HTTP_200_OK)
            else:
                message = {
                    "detail": "Error updating user. Please check the fields.",
                    "errors": serializer.errors
                }
                return Response({"message": message}, status=status.HTTP_400_BAD_REQUEST)
        except Http404 as e:
            message = {"detail": str(e)}
            return Response({"message": message}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            message = {"detail": "An error occurred while updating the user.", "error": str(e)}
            return Response({"message": message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class deleteUser(APIView):
    """
    Delete a specific user.
    """
    def get_object(self, id):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
            raise Http404(f"User with id {id} does not exist.")

    def delete(self, request, id, format=None):
        try:
            user = self.get_object(id)
            user.delete()
            message = {"detail": "User deleted successfully."}
            return Response({"message": message}, status=status.HTTP_200_OK)
        except Http404 as e:
            message = {"detail": str(e)}
            return Response({"message": message}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            message = {"detail": "An error occurred while deleting the user.", "error": str(e)}
            return Response({"message": message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
