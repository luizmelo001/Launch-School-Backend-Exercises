#Write a function that converts the temperature from celsius to fahrenheit
#Make sure to enforce the necessary data type coersions
#Handle user input to ensure that ints or floats are being passed

#Write a funtion that converts the temprature from Celsius to Farenheit

def convert_to_fahrenheit(celsius_temp):
    #handle user input
    #checks if the value is an int of a float
    if not isinstance(celsius_temp, (int, float)):
        raise TypeError("Input must be a number (in or float)")
    
    try:
        #convert to float for consistency if it's an int
        celsius_float = float(celsius_temp)
        fahrenheit = (celsius_temp * 9/5) + 32
        return round(fahrenheit, 2)
    except ValueError:
        raise ValueError("The input cannot be converted to a number")

print(convert_to_fahrenheit(32))
