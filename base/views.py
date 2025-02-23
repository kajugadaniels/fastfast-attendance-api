from base.models import *
from account.models import *
from base.serializers import *
from django.db.models import Q
from django.http import Http404
from account.serializers import *
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

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

class showUser(APIView):
    """
    Retrieve detailed information about a specific user.
    """
    permission_classes = [IsAuthenticated]

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
            return Response(
                {"data": serializer.data, "message": message},
                status=status.HTTP_200_OK
            )
        except Http404 as e:
            message = {"detail": str(e)}
            return Response({"message": message}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            message = {
                "detail": "An error occurred while retrieving the user.",
                "error": str(e)
            }
            return Response({"message": message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class editUser(APIView):
    """
    Update an existing user completely (PUT) or partially (PATCH).
    """
    permission_classes = [IsAuthenticated]

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
                return Response(
                    {"data": serializer.data, "message": message},
                    status=status.HTTP_200_OK
                )
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
            message = {
                "detail": "An unexpected error occurred while updating the user.",
                "error": str(e)
            }
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
                return Response(
                    {"data": serializer.data, "message": message},
                    status=status.HTTP_200_OK
                )
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
            message = {
                "detail": "An unexpected error occurred while updating the user.",
                "error": str(e)
            }
            return Response({"message": message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class deleteUser(APIView):
    """
    Delete a specific user.
    """
    permission_classes = [IsAuthenticated]

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
            message = {
                "detail": "An unexpected error occurred while deleting the user.",
                "error": str(e)
            }
            return Response({"message": message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class getEmployees(APIView):
    """
    Retrieve a list of all employees.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        try:
            employees = Employee.objects.all().order_by('-created_at')
            serializer = EmployeeSerializer(employees, many=True)
            message = {"detail": "Successfully retrieved all employees."}
            return Response(
                {"data": serializer.data, "message": message},
                status=status.HTTP_200_OK
            )
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
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        try:
            serializer = EmployeeSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()  # calls create() in EmployeeSerializer
                message = {"detail": "Employee created successfully."}
                return Response(
                    {"data": serializer.data, "message": message},
                    status=status.HTTP_201_CREATED
                )
            else:
                message = {
                    "detail": "Error creating employee. Please check the fields.",
                    "errors": serializer.errors
                }
                return Response({"message": message}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            message = {
                "detail": "An unexpected error occurred while creating the employee.",
                "error": str(e)
            }
            return Response({"message": message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class showEmployee(APIView):
    """
    Retrieve detailed information about a specific employee, including:
      - Basic employee info.
      - Full attendance history: each record includes:
            - attendance_date (formatted as "YYYY-MM-DD"),
            - time (formatted as "YYYY-MM-DD HH:MM:SS", or null if unavailable),
            - attendance_status ("Present" if attended is True, "Absent" otherwise),
            - food_menu: an array containing one object with the food menu's name and price if available,
              or an empty array if not.
      - Total earnings computed as the sum of the food menu prices for all attended records.
      - Recent activities (e.g., the last 5 attendance records).
    
    Note: The legacy salary field and related functionality have been removed. All earnings
    are now derived solely from the associated food menu price.
    """
    permission_classes = [AllowAny]

    def get_object(self, id):
        try:
            return Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            raise Http404(f"Employee with id {id} does not exist.")

    def get(self, request, id, format=None):
        try:
            employee = self.get_object(id)
            # Serialize basic employee info.
            employee_serializer = EmployeeSerializer(employee, context={'request': request})
            
            # Retrieve the complete attendance history for the employee,
            # ordered by descending time_in.
            attendance_qs = Attendance.objects.filter(employee=employee).order_by('-time_in')
            
            # Compute total earnings using the food_menu price for attended records.
            total_earnings = sum(
                record.food_menu.price 
                for record in attendance_qs 
                if record.attended and record.food_menu
            )
            
            # Build the full attendance history array.
            attendance_history = []
            for record in attendance_qs:
                record_status = "Present" if record.attended else "Absent"
                record_time = record.time_in.strftime('%Y-%m-%d %H:%M:%S') if record.time_in else None
                # Prepare food_menu details as an array.
                if record.food_menu:
                    food_menu_data = [{
                        "name": record.food_menu.name,
                        "price": str(record.food_menu.price)
                    }]
                else:
                    food_menu_data = []
                attendance_history.append({
                    "attendance_date": record.attendance_date.strftime('%Y-%m-%d'),
                    "time": record_time,
                    "attendance_status": record_status,
                    "food_menu": food_menu_data,
                })
            
            # Extract recent activities (last 5 records).
            recent_activities_qs = attendance_qs[:5]
            recent_activities = []
            for record in recent_activities_qs:
                record_status = "Present" if record.attended else "Absent"
                record_time = record.time_in.strftime('%Y-%m-%d %H:%M:%S') if record.time_in else None
                if record.food_menu:
                    food_menu_data = [{
                        "name": record.food_menu.name,
                        "price": str(record.food_menu.price)
                    }]
                else:
                    food_menu_data = []
                recent_activities.append({
                    "attendance_date": record.attendance_date.strftime('%Y-%m-%d'),
                    "time": record_time,
                    "attendance_status": record_status,
                    "food_menu": food_menu_data,
                })
            
            data = {
                "employee": employee_serializer.data,
                "attendance_history": attendance_history,
                "total_earnings": str(total_earnings),
                "recent_activities": recent_activities
            }
            
            message = {"detail": "Employee retrieved successfully with complete attendance details."}
            return Response({"data": data, "message": message}, status=status.HTTP_200_OK)
        
        except Http404 as e:
            message = {"detail": str(e)}
            return Response({"message": message}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            message = {
                "detail": "An error occurred while retrieving the employee details.",
                "error": str(e)
            }
            return Response({"message": message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class editEmployee(APIView):
    """
    Update an existing employee completely (PUT) or partially (PATCH).
    """
    permission_classes = [IsAuthenticated]

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
                serializer.save()  # calls update() in EmployeeSerializer
                message = {"detail": "Employee updated successfully (full update)."}
                return Response(
                    {"data": serializer.data, "message": message},
                    status=status.HTTP_200_OK
                )
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
            message = {
                "detail": "An unexpected error occurred while updating the employee.",
                "error": str(e)
            }
            return Response({"message": message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def patch(self, request, id, format=None):
        """
        Handle partial update of an employee.
        """
        try:
            employee = self.get_object(id)
            serializer = EmployeeSerializer(employee, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()  # calls update() in EmployeeSerializer
                message = {"detail": "Employee updated successfully (partial update)."}
                return Response(
                    {"data": serializer.data, "message": message},
                    status=status.HTTP_200_OK
                )
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
            message = {
                "detail": "An unexpected error occurred while updating the employee.",
                "error": str(e)
            }
            return Response({"message": message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class deleteEmployee(APIView):
    """
    Delete a specific employee.
    """
    permission_classes = [IsAuthenticated]

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
            message = {
                "detail": "An unexpected error occurred while deleting the employee.",
                "error": str(e)
            }
            return Response({"message": message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class GetFoodMenus(APIView):
    """
    Retrieve a list of all food menus.
    """
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        menus = FoodMenu.objects.all()
        serializer = FoodMenuSerializer(menus, many=True)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)

class AddFoodMenu(APIView):
    """
    Create a new food menu item.
    """
    def post(self, request, format=None):
        serializer = FoodMenuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data, "message": "Food item created successfully."}, status=status.HTTP_201_CREATED)
        return Response({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class ShowFoodMenu(APIView):
    """
    Retrieve a single food menu item by its ID.
    """
    def get_object(self, id):
        try:
            return FoodMenu.objects.get(id=id)
        except FoodMenu.DoesNotExist:
            raise Http404(f"Food item with id {id} does not exist.")

    def get(self, request, id, format=None):
        menu = self.get_object(id)
        serializer = FoodMenuSerializer(menu)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)

class EditFoodMenu(APIView):
    """
    Update an existing food menu item.
    """
    def get_object(self, id):
        try:
            return FoodMenu.objects.get(id=id)
        except FoodMenu.DoesNotExist:
            raise Http404(f"Food item with id {id} does not exist.")

    def put(self, request, id, format=None):
        menu = self.get_object(id)
        serializer = FoodMenuSerializer(menu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data, "message": "Food item updated successfully."}, status=status.HTTP_200_OK)
        return Response({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id, format=None):
        menu = self.get_object(id)
        serializer = FoodMenuSerializer(menu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data, "message": "Food item updated successfully (partial)."}, status=status.HTTP_200_OK)
        return Response({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class DeleteFoodMenu(APIView):
    """
    Delete a specific food menu item.
    """
    def get_object(self, id):
        try:
            return FoodMenu.objects.get(id=id)
        except FoodMenu.DoesNotExist:
            raise Http404(f"Food item with id {id} does not exist.")

    def delete(self, request, id, format=None):
        menu = self.get_object(id)
        menu.delete()
        return Response({"message": "Food item deleted successfully."}, status=status.HTTP_200_OK)
class getAttendances(APIView):
    """
    Retrieve a list of all employees with their complete attendance history.
    
    For each employee, only the following fields are returned at the top level:
        - employee_id, name, phone, gender, and position.
    
    All attendance records for that employee (including today's and past records)
    are returned inside the `attendance_history` array. Each record in the array
    contains:
        - attendance_date (formatted as "YYYY-MM-DD")
        - time (formatted as "YYYY-MM-DD HH:MM:SS", or null if not available)
        - attendance_status ("Present" if the record's attended flag is True; "Absent" otherwise)
        - food_menu: an array with a single object containing the food menu's name and price,
          or an empty array if no food menu is associated.
    
    This professional implementation avoids duplication by placing all attendance data
    in the history array.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        try:
            # Retrieve all employees ordered by descending id
            employees = Employee.objects.all().order_by('-id')
            results = []

            for emp in employees:
                # Retrieve all attendance records for the employee (today and past dates)
                attendance_records = Attendance.objects.filter(employee=emp).order_by('-attendance_date')
                history_list = []

                for record in attendance_records:
                    record_status = "Present" if record.attended else "Absent"
                    record_time = record.time_in.strftime('%Y-%m-%d %H:%M:%S') if record.time_in else None

                    # Prepare food menu info as an array (if available)
                    if record.food_menu:
                        food_menu_data = [{
                            "name": record.food_menu.name,
                            "price": str(record.food_menu.price)
                        }]
                    else:
                        food_menu_data = []

                    history_list.append({
                        "attendance_date": record.attendance_date.strftime('%Y-%m-%d'),
                        "time": record_time,
                        "attendance_status": record_status,
                        "food_menu": food_menu_data,
                    })

                results.append({
                    "employee_id": emp.id,
                    "name": emp.name,
                    "phone": emp.phone,
                    "gender": emp.gender,
                    "position": emp.position,
                    "attendance_history": history_list,
                })

            message = {
                "detail": "Successfully retrieved all employees with complete attendance history."
            }
            return Response({"data": results, "message": message}, status=status.HTTP_200_OK)
        except Exception as e:
            message = {
                "detail": "An error occurred while retrieving attendance records.",
                "error": str(e)
            }
            return Response({"message": message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class addAttendance(APIView):
    """
    Create a new attendance record for an employee based on finger_id.
    Enforces the 12-hour rule for consecutive taps.
    Adds logic for 'attended' boolean to track presence/absence.
    Now includes food_menu selection for calculating salary.
    """
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        try:
            finger_id = request.data.get('finger_id')
            attended = request.data.get('attended', True)
            food_menu_id = request.data.get('food_menu')

            if finger_id is None:
                return Response({
                    "message": {
                        "detail": "finger_id is required to record attendance."
                    }
                }, status=status.HTTP_400_BAD_REQUEST)

            # Retrieve employee via the provided finger_id
            try:
                employee = Employee.objects.get(finger_id=finger_id)
            except Employee.DoesNotExist:
                return Response({
                    "message": {
                        "detail": f"No employee found with finger_id={finger_id}"
                    }
                }, status=status.HTTP_404_NOT_FOUND)

            # Retrieve food menu item
            if food_menu_id:
                try:
                    food_menu = FoodMenu.objects.get(id=food_menu_id)
                except FoodMenu.DoesNotExist:
                    return Response({
                        "message": {
                            "detail": f"No food item found with id={food_menu_id}"
                        }
                    }, status=status.HTTP_404_NOT_FOUND)
            else:
                food_menu = None

            # Check if the last attendance was within 12 hours
            last_attendance = Attendance.objects.filter(employee=employee).order_by('-time_in').first()
            if last_attendance:
                time_diff = timezone.now() - last_attendance.time_in
                if time_diff < timedelta(hours=12):
                    return Response({
                        "message": {
                            "detail": (
                                f"You have already tapped in the last 12 hours. "
                                f"Please wait at least {(12 - time_diff.seconds//3600)} more hour(s)."
                            )
                        }
                    }, status=status.HTTP_400_BAD_REQUEST)

            # If attended=False, then salary = 0
            salary = food_menu.price if attended and food_menu else 0

            data = {
                "employee": employee.id,
                "finger_id": employee.finger_id,
                "attended": attended,
                "food_menu": food_menu.id if food_menu else None,
                "salary": str(salary)
            }

            serializer = AttendanceSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                message = {
                    "detail": (
                        "Attendance recorded successfully. "
                        f"{'Present' if attended else 'Absent'} for {employee.name}."
                    )
                }
                return Response(
                    {"data": serializer.data, "message": message},
                    status=status.HTTP_201_CREATED
                )
            else:
                message = {
                    "detail": "Error creating attendance. Please check the fields.",
                    "errors": serializer.errors
                }
                return Response({"message": message}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            message = {
                "detail": "An unexpected error occurred while creating the attendance record.",
                "error": str(e)
            }
            return Response({"message": message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class showAttendance(APIView):
    """
    Retrieve detailed information about a single Employee's entire attendance history,
    including the total amount of salary earned.
    
    NOTE: We interpret the 'id' in the URL as the 'employee_id' now, not attendance_id.
          This allows a full history for that Employee.
    """
    permission_classes = [IsAuthenticated]

    def get_employee(self, id):
        try:
            return Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            raise Http404(f"Employee with ID {id} does not exist.")

    def get(self, request, id, format=None):
        """
        Returns:
          - Employee basic info
          - Full attendance history (present & absent)
          - total_salary: sum of all salary across the Employee’s attendance
        """
        try:
            employee = self.get_employee(id)
            # Retrieve all attendance records for this employee
            attendance_qs = Attendance.objects.filter(employee=employee).order_by('-time_in')
            
            # Calculate total salary by summing salary (Decimal sum).
            total_salary = sum(record.salary for record in attendance_qs)

            # We can serialize attendance records individually
            attendance_serializer = AttendanceSerializer(attendance_qs, many=True)

            # If you also want to show the employee's own details in the response:
            employee_serializer = EmployeeSerializer(employee)

            # Build a custom response structure
            data = {
                "employee": employee_serializer.data,
                "attendance_history": attendance_serializer.data,
                "total_salary": str(total_salary)
            }

            message = {"detail": "Successfully retrieved detailed attendance info."}
            return Response(
                {"data": data, "message": message},
                status=status.HTTP_200_OK
            )
        except Http404 as e:
            # Employee not found
            message = {"detail": str(e)}
            return Response({"message": message}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            # Other unforeseen errors
            message = {
                "detail": "An error occurred while retrieving attendance information.",
                "error": str(e)
            }
            return Response({"message": message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class editAttendance(APIView):
    """
    Update an existing attendance record completely (PUT) or partially (PATCH).
    Typically, you might not change the time_in for an attendance record,
    but let's keep it open in case you need corrections or updates.
    """
    permission_classes = [IsAuthenticated]

    def get_object(self, id):
        try:
            return Attendance.objects.get(id=id)
        except Attendance.DoesNotExist:
            raise Http404(f"Attendance record with id {id} does not exist.")

    def put(self, request, id, format=None):
        """
        Full update of an attendance record.
        """
        try:
            attendance = self.get_object(id)
            serializer = AttendanceSerializer(attendance, data=request.data)
            if serializer.is_valid():
                serializer.save()
                message = {"detail": "Attendance record fully updated successfully."}
                return Response(
                    {"data": serializer.data, "message": message},
                    status=status.HTTP_200_OK
                )
            else:
                message = {
                    "detail": "Error updating attendance record. Check the fields.",
                    "errors": serializer.errors
                }
                return Response({"message": message}, status=status.HTTP_400_BAD_REQUEST)
        except Http404 as e:
            message = {"detail": str(e)}
            return Response({"message": message}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            message = {
                "detail": "An unexpected error occurred while updating the attendance record.",
                "error": str(e)
            }
            return Response({"message": message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def patch(self, request, id, format=None):
        """
        Partial update of an attendance record.
        """
        try:
            attendance = self.get_object(id)
            serializer = AttendanceSerializer(attendance, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                message = {"detail": "Attendance record partially updated successfully."}
                return Response(
                    {"data": serializer.data, "message": message},
                    status=status.HTTP_200_OK
                )
            else:
                message = {
                    "detail": "Error updating attendance record. Check the fields.",
                    "errors": serializer.errors
                }
                return Response({"message": message}, status=status.HTTP_400_BAD_REQUEST)
        except Http404 as e:
            message = {"detail": str(e)}
            return Response({"message": message}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            message = {
                "detail": "An unexpected error occurred while updating the attendance record.",
                "error": str(e)
            }
            return Response({"message": message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class deleteAttendance(APIView):
    """
    Delete a specific attendance record by ID.
    """
    permission_classes = [IsAuthenticated]

    def get_object(self, id):
        try:
            return Attendance.objects.get(id=id)
        except Attendance.DoesNotExist:
            raise Http404(f"Attendance record with id {id} does not exist.")

    def delete(self, request, id, format=None):
        try:
            attendance = self.get_object(id)
            attendance.delete()
            message = {"detail": "Attendance record deleted successfully."}
            return Response({"message": message}, status=status.HTTP_200_OK)
        except Http404 as e:
            message = {"detail": str(e)}
            return Response({"message": message}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            message = {
                "detail": "An unexpected error occurred while deleting the attendance record.",
                "error": str(e)
            }
            return Response({"message": message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
