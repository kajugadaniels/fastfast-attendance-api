import re
from base.models import *
from rest_framework import serializers

class EmployeeSerializer(serializers.ModelSerializer):
    """
    A more 'professional' EmployeeSerializer with custom validations.
    """

    class Meta:
        model = Employee
        excluded = ['created_at', 'updated_at']
        fields = '__all__'

    def validate_phone(self, value):
        """
        Validate that the phone number is 10-15 digits (with optional leading '+').
        Adjust the regex or logic to match your business rules.
        """
        # Example pattern: optional '+' followed by 10-15 digits
        pattern = r'^\+?\d{10,15}$'
        if not re.match(pattern, value):
            raise serializers.ValidationError(
                "Phone number must be 10-15 digits, optionally starting with '+'"
            )
        return value

    def validate_salary(self, value):
        if value < 0:
            raise serializers.ValidationError("Salary cannot be negative.")
        return value

    def validate_finger_id(self, value):
        if value <= 0:
            raise serializers.ValidationError("Finger ID must be greater than 0.")
        return value

    def create(self, validated_data):
        """
        Create an Employee instance, ensuring model-level clean() is called.
        """
        employee = Employee(**validated_data)
        employee.clean()
        employee.save()
        return employee

    def update(self, instance, validated_data):
        """
        Update an Employee instance, ensuring model-level clean() is called.
        """
        for attr, val in validated_data.items():
            setattr(instance, attr, val)
        instance.clean()
        instance.save()
        return instance

class AttendanceSerializer(serializers.ModelSerializer):
    """
    Serializer for Attendance model.
    Includes 'attended' to indicate presence/absence.
    """
    class Meta:
        model = Attendance
        fields = ['id', 'employee', 'finger_id', 'time_in', 'salary', 'attended']
        read_only_fields = ['time_in']

    def create(self, validated_data):
        """
        Override create to ensure model-level clean is called.
        """
        attendance = Attendance(**validated_data)
        attendance.clean()
        attendance.save()
        return attendance

    def update(self, instance, validated_data):
        """
        Override update to ensure model-level clean is called.
        """
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.clean()
        instance.save()
        return instance