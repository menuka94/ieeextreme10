numbers_input = [int(x.strip()) for x in input().split()]
#numbers_input = [3,1,2,3,2]

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

    return nextList

lists = [numbers_input]

while True:
    nextList = get_next_list(lists[-1])
    if(nextList in lists):
        lists.append(nextList)
        break
    else:
        lists.append(nextList)

# for eachList in lists:
#     print(eachList)

depth = lists.index(lists[-1])
# print('\nDepth: ' + str(depth))
# print(depth)

"""
so the height is
the length of the longest sequence of unique
configurations that leads to the current configuration
"""

total = sum(numbers_input)
reversed_list = numbers_input[::-1]
height = len(reversed_list) - reversed_list.index(1)
print(str(depth) + ' ' + str(height))
