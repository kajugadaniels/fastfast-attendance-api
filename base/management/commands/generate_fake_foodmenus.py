import random
from base.models import FoodMenu
from decimal import Decimal
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Generate at least 40 fake food menus'

    def handle(self, *args, **kwargs):
        food_names = [
            "Burger", "Pizza", "Pasta", "Sandwich", "Salad", "Soup", "Sushi", "Steak",
            "Tacos", "Curry", "Burrito", "Fried Rice", "Shawarma", "Ramen", "Dumplings",
            "Grilled Chicken", "Fish and Chips", "Kebab", "Noodles", "Waffles",
            "Pancakes", "Ice Cream", "Donuts", "Nachos", "Quesadilla", "Falafel", "Chow Mein",
            "Hot Dog", "Mac and Cheese", "Pho", "Lasagna", "Meatballs", "Mashed Potatoes",
            "Onion Rings", "Spring Rolls", "Biryani", "Poutine", "Stuffed Peppers", "Tofu Stir Fry",
            "Chicken Wings", "Beef Stroganoff", "Pad Thai", "Gnocchi", "Tuna Salad", "Lamb Chops"
        ]

        created_count = 0

        for name in food_names:
            # Avoid duplicates
            if not FoodMenu.objects.filter(name=name).exists():
                price = Decimal(random.randint(1000, 9999))
                FoodMenu.objects.create(
                    name=name,
                    price=price
                )
                created_count += 1

        self.stdout.write(self.style.SUCCESS(f'Successfully created {created_count} unique fake food menus'))
