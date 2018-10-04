from copy import deepcopy


# Quicksort
# [5 1 7 4 2 3] pivot 5
# [1 4 2 3] 5 [7]

# Quicksort 2
# 1 4 2 3
# [] 1 [4 2 3]
# [7] return 7

# Quicksort 3
#  [4 2 3]
# [2 3] 4 []

# Quicksort 4
# 3 2 4
# 2 3 4

# Quicksort 5
#

def partition(list_numbers):
    first = list_numbers[0]
    lower = []
    bigger = []
    for i in list_numbers[1:]:
        if i <= first:
            lower.append(i)
        else:
            bigger.append(i)
    return lower + [first] + bigger, len(lower)


def quick_sort(list_numbers):
    if list_numbers == []:
        return []
    if len(list_numbers) == 1:
        return list_numbers
    partioned, index = partition(list_numbers)
    return quick_sort(partioned[:index]) + [partioned[index]] + quick_sort(partioned[index + 1:])
