from django.db import models
from django.core.exceptions import ValidationError

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
