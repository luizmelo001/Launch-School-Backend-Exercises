def double(num):
    global int_val
    int_val = num * 2
    return int_val

int_val = 2
int_val = double(int_val)  # Assign the result back to int_val

print(int_val)  # This will now print 4