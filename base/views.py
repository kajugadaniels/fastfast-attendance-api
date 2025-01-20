from account.models import User
from base.models import Employee
from django.http import Http404
from account.serializers import UserSerializer
from base.serializers import EmployeeSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

# User Views
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

# Employee Views
class getEmployees(APIView):
    """
    Retrieve a list of all employees.
    """
    def get(self, request, format=None):
        try:
            employees = Employee.objects.all()
            serializer = EmployeeSerializer(employees, many=True)
            message = {"detail": "Successfully retrieved all employees."}
            return Response({"data": serializer.data, "message": message}, status=status.HTTP_200_OK)
        except Exception as e:
            message = {
                "detail": "An error occurred while retrieving employees.",
                "error": str(e)
            }
            return Response({"message": message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class addEmployee(APIView):
    """
    Create a new employee.
    """
    def post(self, request, format=None):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            message = {"detail": "Employee created successfully."}
            return Response({"data": serializer.data, "message": message}, status=status.HTTP_201_CREATED)
        else:
            message = {
                "detail": "Error creating employee. Please check the fields.",
                "errors": serializer.errors
            }
            return Response({"message": message}, status=status.HTTP_400_BAD_REQUEST)


class showEmployee(APIView):
    """
    Retrieve detailed information about a specific employee.
    """
    def get_object(self, id):
        try:
            return Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            raise Http404(f"Employee with id {id} does not exist.")

    def get(self, request, id, format=None):
        try:
            employee = self.get_object(id)
            serializer = EmployeeSerializer(employee)
            message = {"detail": "Employee retrieved successfully."}
            return Response({"data": serializer.data, "message": message}, status=status.HTTP_200_OK)
        except Http404 as e:
            message = {"detail": str(e)}
            return Response({"message": message}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            message = {"detail": "An error occurred while retrieving the employee.", "error": str(e)}
            return Response({"message": message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class editEmployee(APIView):
    """
    Update an existing employee completely (PUT) or partially (PATCH).
    """
    def get_object(self, id):
        try:
            return Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            raise Http404(f"Employee with id {id} does not exist.")

    def put(self, request, id, format=None):
        """
        Handle complete update of an employee.
        """
        try:
            employee = self.get_object(id)
            serializer = EmployeeSerializer(employee, data=request.data)
            if serializer.is_valid():
                serializer.save()
                message = {"detail": "Employee updated successfully."}
                return Response({"data": serializer.data, "message": message}, status=status.HTTP_200_OK)
            else:
                message = {
                    "detail": "Error updating employee. Please check the fields.",
                    "errors": serializer.errors
                }
                return Response({"message": message}, status=status.HTTP_400_BAD_REQUEST)
        except Http404 as e:
            message = {"detail": str(e)}
            return Response({"message": message}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            message = {"detail": "An error occurred while updating the employee.", "error": str(e)}
            return Response({"message": message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def patch(self, request, id, format=None):
        """
        Handle partial update of an employee.
        """
        try:
            employee = self.get_object(id)
            serializer = EmployeeSerializer(employee, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                message = {"detail": "Employee updated successfully."}
                return Response({"data": serializer.data, "message": message}, status=status.HTTP_200_OK)
            else:
                message = {
                    "detail": "Error updating employee. Please check the fields.",
                    "errors": serializer.errors
                }
                return Response({"message": message}, status=status.HTTP_400_BAD_REQUEST)
        except Http404 as e:
            message = {"detail": str(e)}
            return Response({"message": message}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            message = {"detail": "An error occurred while updating the employee.", "error": str(e)}
            return Response({"message": message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class deleteEmployee(APIView):
    """
    Delete a specific employee.
    """
    def get_object(self, id):
        try:
            return Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            raise Http404(f"Employee with id {id} does not exist.")

    def delete(self, request, id, format=None):
        try:
            employee = self.get_object(id)
            employee.delete()
            message = {"detail": "Employee deleted successfully."}
            return Response({"message": message}, status=status.HTTP_200_OK)
        except Http404 as e:
            message = {"detail": str(e)}
            return Response({"message": message}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            message = {"detail": "An error occurred while deleting the employee.", "error": str(e)}
            return Response({"message": message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
