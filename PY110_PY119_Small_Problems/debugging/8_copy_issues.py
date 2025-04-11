"""
We have a list of lists and want to duplicate it. 
After making the copy, we modify the original list, but the copied list also seems to be affected:
"""

import copy

original = [[1], [2], [3]]
copied = copy.deepcopy(original)

original[0][0] = 99

print(copied[0] == [1])