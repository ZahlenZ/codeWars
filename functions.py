from itertools import groupby

# First function challenge

def unique_in_order(iterable):
    return [k for (k, _) in groupby(iterable)]

unique_in_order = lambda l: [z for i, z in enumerate(l) if i == 0 or l[i - 1] != z]

def unique_in_order(iterable):
    return [ ch for i, ch in enumerate(iterable) if i == 0 or ch != iterable[i - 1] ]


#%%
import random

def sort_faster(array):
    if len(array) < 2:
        return array
    
    less_than, same, greater_than = [], [], []

    pivot = array[random.randint(0, len(array) - 1)]

    for item in array:
        if item < pivot:
            less_than.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            greater_than.append(item)
    
    return sort_faster(less_than) + same + sort_faster(greater_than)

array = [1, 2, -3, 4, 5, -10]

sort_faster(array)
