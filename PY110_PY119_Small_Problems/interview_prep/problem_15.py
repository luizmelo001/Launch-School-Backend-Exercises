"""
Write a function sort_products that takes a list of product dictionaries. Each product has a 'name', 'category', and 'price'. 
The function should return a new list of products sorted first by category (alphabetically), then by price (lowest to highest), 
and finally by name (alphabetically).
"""

def sort_products(lst):
    return sorted(lst, key= lambda x: (x["category"], x["price"], x["name"]))

# Example usage:
products = [
    {"name": "Laptop", "category": "Electronics", "price": 1200},
    {"name": "Headphones", "category": "Electronics", "price": 100},
    {"name": "Coffee Maker", "category": "Kitchen", "price": 80},
    {"name": "Blender", "category": "Kitchen", "price": 80},
    {"name": "Smartphone", "category": "Electronics", "price": 800}
]

# Should return products in this order:
expected = [
   {"name": "Headphones", "category": "Electronics", "price": 100},
   {"name": "Smartphone", "category": "Electronics", "price": 800},
   {"name": "Laptop", "category": "Electronics", "price": 1200},
   {"name": "Blender", "category": "Kitchen", "price": 80},
   {"name": "Coffee Maker", "category": "Kitchen", "price": 80}
 ]

print(sort_products(products) == expected)
