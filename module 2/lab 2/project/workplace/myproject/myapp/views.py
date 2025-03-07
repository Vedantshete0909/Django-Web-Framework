from django.http import HttpResponse  # Import HttpResponse
from django.shortcuts import render  # Optional for future use

def drinks(request, drink_name):
    # Step 3: Create dictionary with drink types
    drink = {
        'mocha': 'type of coffee',
        'tea': 'type of beverage',
        'lemonade': 'type of refreshment'
    }

    # Step 4: Get the drink description from the dictionary
    choice_of_drink = drink.get(drink_name, "Sorry, this drink is not available.")

    # Step 5: Return an HttpResponse with formatted HTML
    return HttpResponse(f"<h2>{drink_name}</h2>{choice_of_drink}")