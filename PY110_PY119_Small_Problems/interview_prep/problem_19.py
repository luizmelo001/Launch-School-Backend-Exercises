"""
Write a function that counts similar letters in a string

Algorithm:
    -creater a counter
    -iterate in pairs and check if the letters are the same

"""
def count_duplicates(string):
    counter = 0

    for i in range(0,len(string)-1, 2):
        if string[i] == string[i + 1]:
            counter += 1

    return counter

print(count_duplicates('aabbccc'))  # 3
print(count_duplicates('aabbcccc')) # 4