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
