
def tip_calculator():
    
    print("What is the bill?")
    bill = float(input())

    print("What is the tip percentage?")
    tip_percentage = float(input())

    tip = (bill * tip_percentage)/100
    total = bill + tip

    print(f"The tip is {tip:.2f}")
    print(f"The total is {total:.2f}")

tip_calculator()