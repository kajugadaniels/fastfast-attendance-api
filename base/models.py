import os
import random
from django.db import models
from django.utils import timezone
from django.dispatch import receiver
from django.utils.text import slugify
from imagekit.processors import ResizeToFill
from django.db.models.signals import pre_save
from imagekit.models import ProcessedImageField
from django.core.exceptions import ValidationError

def employee_image_path(instance, filename):
    base_filename, file_extension = os.path.splitext(filename)
    return f'employee/profile/employee_{slugify(instance.name)}_{instance.phone}_{instance.finger_id}{file_extension}'

class Employee(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    name = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=15, unique=True, null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='O')
    position = models.CharField(max_length=50, null=True, blank=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    finger_id = models.PositiveIntegerField(unique=True, null=True, blank=True)
    image = ProcessedImageField(
        upload_to=employee_image_path,
        processors=[ResizeToFill(1270, 1270)],
        format='JPEG',
        options={'quality': 90},
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def clean(self):
        """
        Perform additional model-level validations.
        """
        # Ensure salary is not negative
        if self.salary < 0:
            raise ValidationError("Salary cannot be negative.")
        
        # Example check if phone is numeric (allowing + sign). 
        # Adjust your regex/condition for your needs.
        if not self.phone.replace('+', '').isdigit():
            raise ValidationError("Phone number must contain only digits (optionally starting with +).")

        # finger_id is PositiveIntegerField, so Django already ensures >= 1.
        # But if you want more constraints (e.g., a max limit), you could add them here.
        super().clean()

# Signal to automatically generate finger_id before saving an Employee
@receiver(pre_save, sender=Employee)
def generate_finger_id(sender, instance, **kwargs):
    """
    Auto-generate the `finger_id` for a new Employee before saving.
    Ensure the `finger_id` is unique and has a length of 5 digits.
    """
    if instance.finger_id is None:
        while True:
            # Generate a random 5-digit number (ensuring uniqueness)
            finger_id = random.randint(10000, 99999)
            if not Employee.objects.filter(finger_id=finger_id).exists():
                instance.finger_id = finger_id
                break

class Attendance(models.Model):
    """
    Model representing an attendance record for an Employee.
    If 'attended' is False, the employee is marked absent
    and 'salary' will be 0.
    """
    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name='attendance_records'
    )
    finger_id = models.PositiveIntegerField()
    time_in = models.DateTimeField(auto_now_add=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    attended = models.BooleanField(default=True)

    class Meta:
        ordering = ['-time_in']

    def __str__(self):
        return f"Attendance({self.employee.name}) on {self.time_in.strftime('%Y-%m-%d %H:%M:%S')}"

    def clean(self):
        """
        Optional validation to ensure the finger_id
        matches the assigned Employee's finger_id (if required).
        """
        if self.finger_id != self.employee.finger_id:
            raise ValidationError("finger_id does not match the Employee's finger_id.")

        # If not attended, salary is expected to be 0
        if not self.attended and self.salary != 0:
            raise ValidationError("If 'attended' is False, salary must be 0.")
        super().clean()