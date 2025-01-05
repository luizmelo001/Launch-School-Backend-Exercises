# In this exercise, you will write an xor function that takes two arguments, and returns True 
# if exactly one of its arguments is truthy, False otherwise.

def xor(val1, val2):
    return (val1 and not val2) or (not val1 and val2)

   

print(xor(5, 0))
print(xor(False, True))
print(xor(1, 1))
print(xor(True, True))