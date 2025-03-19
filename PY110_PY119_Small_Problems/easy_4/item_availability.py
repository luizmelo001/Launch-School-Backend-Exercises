"""
Building on the previous exercise, write a function that 
returns True or False based on whether or not an inventory item (an ID number) is available. 
As before, the function takes two arguments: an item ID and a list of transactions. 
The function should return True only if the sum of the quantity values of the item's transactions is greater than zero. 
Notice that there is a movement property in each transaction object. A movement value of 'out' will decrease the item's quantity.

Problem:
    input: list of dictionaries
    output: boolean that represents if the quantity is greater than 0 or not

Examples:

Data Type:

Algorithm: (break a bigger problem into small chunks)
    -Initialize a counter to keep track of the quantity
    -Loop through the movement and check if it is "in" or "out"
    -Subtract or add depending of the result
    -Return true if the quantity is greater than 0, false otherwise
"""

def is_item_available(id_num, transaction_list):
    counter = 0

    for transaction in transaction_list:
        if (transaction["id"] == id_num):
            if transaction["movement"] == "in":
                counter += transaction["quantity"]
            else:
                counter -= transaction["quantity"]
    return counter > 0   


transactions = [
    {"id": 101, "movement": 'in',  "quantity":  5},
    {"id": 105, "movement": 'in',  "quantity": 10},
    {"id": 102, "movement": 'out', "quantity": 17},
    {"id": 101, "movement": 'in',  "quantity": 12},
    {"id": 103, "movement": 'out', "quantity": 20},
    {"id": 102, "movement": 'out', "quantity": 15},
    {"id": 105, "movement": 'in',  "quantity": 25},
    {"id": 101, "movement": 'out', "quantity": 18},
    {"id": 102, "movement": 'in',  "quantity": 22},
    {"id": 103, "movement": 'out', "quantity": 15},
]

print(is_item_available(101, transactions) == False)  # True 
print(is_item_available(103, transactions) == False)  # True
print(is_item_available(105, transactions) == True)   # True