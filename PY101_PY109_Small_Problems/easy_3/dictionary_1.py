# Implement the food_type_validation function. 
# This function should verify if the categorized_foods dictionary matches the VALID_FOOD_TYPES dictionary, 
# allowing for both lists and single string values for different categories.v


VALID_FOOD_TYPES = {
    "vegetarian": ["Salad", "Tofu", "Lentils"],
    "desserts": "Ice Cream",
}

def food_type_validation(categorized_foods):
    for key, value in categorized_foods.items():
        if key not in VALID_FOOD_TYPES:
            return False
        if isinstance(VALID_FOOD_TYPES[key], list) and sorted(VALID_FOOD_TYPES[key]) != sorted(value):
            return False
        if isinstance(VALID_FOOD_TYPES[key], str) and VALID_FOOD_TYPES[key] != value:
            return False
    return True

food_type_validation({
    "vegetarian": ["Tofu", "Salad", "Lentils"],
    "desserts": "Ice Cream",
})