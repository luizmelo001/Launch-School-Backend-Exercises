# Implement a program to merge two sorted lists into a single sorted list

def merge_sort(list_1, list_2):
    combined = list_1 + list_2
    return sorted(combined)


list_a = [1, 3, 5, 7, 9]
list_b = [2, 4, 6, 8, 10]

print(merge_sort(list_a, list_b))
