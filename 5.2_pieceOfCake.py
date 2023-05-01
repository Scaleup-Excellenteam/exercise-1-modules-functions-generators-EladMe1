def calculate_recipe_price(recipe, **kwargs):
    total_price = 0
    optional_ingredients = []
    # Check if optional argument is provided and assign it to optional_ingredients list.
    for key, value in kwargs.items():
        if key == "optional":
            optional_ingredients = value
    # Calculate the total price of the recipe.
    for ingredient, percentage in kwargs.items():
        if ingredient in recipe and ingredient not in optional_ingredients:
            total_price += recipe[ingredient] * (percentage / 100)

    return total_price