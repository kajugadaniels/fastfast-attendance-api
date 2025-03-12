import random
from faker import Faker
from base.models import *
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Generate fake employees'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # List of example Rwandan names and European names
        rwandan_names = ['Kanyarwanda', 'Munyaneza', 'Nshuti', 'Mugisha', 'Kamanzi', 'Nkusi', 'Byukusenge', 'Ntakirutimana']
        european_names = ['John', 'Michael', 'David', 'Thomas', 'Sebastian', 'Oliver', 'Liam', 'Lucas']

        for i in range(1, 301):  # Loop to create 300 employees
            name = f"{random.choice(rwandan_names)} {random.choice(european_names)}"
            phone = fake.phone_number()
            phone = ''.join(filter(str.isdigit, phone))[:10]  # Ensure the phone number is 10 digits long
            gender = random.choice(['M', 'F', 'O'])
            # 70% chance for "Casual", 30% chance for "Staff"
            position = random.choices(['Casual', 'Staff'], weights=[0.7, 0.3], k=1)[0]

            # Create Employee (finger_id will be auto-generated)
            Employee.objects.create(
                name=name,
                phone=phone,
                gender=gender,
                position=position,
            )

        self.stdout.write(self.style.SUCCESS('Successfully created 300 fake employees'))
