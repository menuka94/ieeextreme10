numbers_input = [4, 3, 1]

def get_next_list(numbers_param):
    numbers = numbers_param[:]
    numbers.extend([0 for x in range(100 - len(numbers))])
    distributor = numbers[0]
    numbers = numbers[1:]  # remove the first element
    j = 0
    while (j < distributor):
        numbers[j] += 1
        j += 1

    nextList = numbers[0:numbers.index(0)]
    print('next list inside method: ' + str(nextList))

    return nextList

lists = [numbers_input]
print(lists)
print(get_next_list(numbers_input))
lists.append(get_next_list(numbers_input))
print(lists)


