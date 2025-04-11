def prompt(message):
    print(f"=> {message}")

def float_math():
    prompt("Enter the first number:")
    float_1 = float(input())

    prompt("Enter the first number:")
    float_2 = float(input())

    prompt(f"{float_1} + {float_2} = {float_1 + float_2}")
    prompt(f"{float_1} - {float_2} = {float_1 - float_2}")
    prompt(f"{float_1} * {float_2} = {float_1 * float_2}")
    prompt(f"{float_1} / {float_2} = {float_1 / float_2}")
    prompt(f"{float_1} // {float_2} = {float_1 // float_2}")
    prompt(f"{float_1} % {float_2} = {float_1 % float_2}")
    prompt(f"{float_1} ** {float_2} = {float_1 ** float_2}")
    
    
float_math()