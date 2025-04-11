# Build a program that asks the user to enter the length and width of a room, in meters, then prints the room's area in both square meters and square feet.

# Note: 1 square meter == 10.7639 square feet

SQ_METERS_TO_SQ_FEET = 10.7639

def room_area():
    length = float(input("Enter the length of the room in meters: "))
    width = float(input("Enter the width of the room in meters: "))

    area_sq_meters = lengthxl * width
    area_sq_feet = area_sq_meters * SQ_METERS_TO_SQ_FEET

    print(f"The area of the room is {area_sq_meters:.2f} square meters.")
    print(f"The area of the room is {area_sq_feet:.2f} square feet.")


room_area()

