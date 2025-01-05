# Build a program that displays when the user will retire and how many years she has to work till retirement.

from datetime import datetime

def when_retire():
    age = int(input("What is your age?"))
    retirement = int(input("At what age would you like to retire?"))
    current_year = datetime.now().year
    retirement_age = retirement - age

    print(f"It's {current_year}. You will retire in {current_year + retirement_age}.")
    print(f"You have only {retirement_age} years of work to go!")


when_retire()