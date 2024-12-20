# Print all odd numbers from 1 to 99, inclusive, with each number on a separate line.
# Bonus Question: Can you solve the problem by iterating over just the odd numbers?

def odd_numbers():
    for n in range(1,99):
        if n % 2 == 1:
            print(n)

odd_numbers()