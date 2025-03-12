import random
from base.models import *
from decimal import Decimal
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Generate fake food menus'

    def handle(self, *args, **kwargs):
        food_names = [
            "Burger",
            "Pizza",
            "Pasta",
            "Sandwich",
            "Salad",
            "Soup",
            "Sushi",
            "Steak",
            "Tacos",
            "Curry"
        ]
        
        # Loop over each food item, generating a random 4-digit price.
        for name in food_names:
            # Generate a random integer between 1000 and 9999.
            price = Decimal(random.randint(1000, 9999))
            FoodMenu.objects.create(
                name=name,
                price=price
            )

        self.stdout.write(self.style.SUCCESS(f'Successfully created {len(food_names)} fake food menus'))
