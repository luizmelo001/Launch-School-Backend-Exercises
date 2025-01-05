

def oddities(lst):
    if len(lst) <= 1:
        return lst
    
    odds = []
    
    for index, item in enumerate(lst):
        if index % 2 == 0:
            odds.append(item)

    return odds


print(oddities([2, 3, 4, 5, 6]))  
print(oddities([1, 2, 3, 4]))        
print(oddities(["abc", "def"]))   
print(oddities([123]))             