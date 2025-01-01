#Write a program that asks for user's name, then greets the user. 
# If the user appends a ! to their name, the computer will 
# yell the greeting (print it using all uppercase).

def greeting(name):
    if not name:
        return("That is not a valid input")
    
    if name.endswith("!"):
        return f"HELLO {name} WHY ARE WE YELLING?"
    
    return f"Hello {name}."


print(greeting("Sue"))
print(greeting("Bob!"))
