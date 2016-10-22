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

#--------------------------------------------# Case I - Reduct 1 from the first element and insert 1 at the beginning
def reduct_the_first(numbers):
    numbers_input = numbers[:]
    if(numbers_input[0] > 1):
        numbers_input[0] -= 1
        numbers_input.insert(0, 1)

    return numbers_input

# Case II - no 1's in the list

# lists = [numbers_input[:]] # insert a copy into the list

def for_no_ones(numbers):
    numbers_input = numbers[:]
    if (1 not in numbers_input):
        addition = 0
        for i in range(len(numbers_input) - 1, -1, -1):
            numbers_input[i] -= 1
            addition += 1
        numbers_input.insert(0, addition)
    return numbers_input

def ones_in_the_middle(numbers):
    numbers_input = numbers[:]
    try:
        position_of_first_one = numbers_input.index(1)
        if (position_of_first_one != 0 and position_of_first_one != len(numbers_input) - 1):
            for i in range(0, position_of_first_one):
                numbers_input[i] -= 1
            numbers_input.insert(0, position_of_first_one)
        return numbers_input
    except:
        return numbers_input
#------- Methods for reverse ----------------

# Case I - Reduct 1 from the first element and insert 1 at the beginning
def reduct_the_first(numbers):
    numbers_input = numbers[:]
    if(numbers_input[0] > 1):
        numbers_input[0] -= 1
        numbers_input.insert(0, 1)

    return numbers_input

# Case II - no 1's in the list

# lists = [numbers_input[:]] # insert a copy into the list

def for_no_ones(numbers):
    numbers_input = numbers[:]
    if (1 not in numbers_input):
        addition = 0
        for i in range(len(numbers_input) - 1, -1, -1):
            numbers_input[i] -= 1
            addition += 1
        numbers_input.insert(0, addition)
    return numbers_input

def ones_in_the_middle(numbers):
    numbers_input = numbers[:]
    try:
        position_of_first_one = numbers_input.index(1)
        if (position_of_first_one != 0 and position_of_first_one != len(numbers_input) - 1):
            for i in range(0, position_of_first_one):
                numbers_input[i] -= 1
            numbers_input.insert(0, position_of_first_one)
        return numbers_input
    except:
        return numbers_input


#--------------------------------------------

height = 1

count1 = 0
test_input = numbers_input[:]
previousLine = ones_in_the_middle(test_input)

while previousLine[0] != 1:
    count1 += 1
    previousLine = ones_in_the_middle(previousLine)

if(height < count1):
    height = count1


# second method
count1 = 0
test_input = numbers_input[:]
previousLine = for_no_ones(test_input)

while previousLine[0] != 1:
    count1 += 1
    previousLine = for_no_ones(previousLine)

if(height < count1):
    height = count1

height = 1

numbers_input = numbers_input[:]
while(1 not in numbers_input):
    numbers_input = for_no_ones(numbers_input)
    height += 1

all_ones = True
for n in numbers_input:
    if n == 1:
        continue
    else:
        all_ones = False

if(all_ones):
    numbers_input = [].append(sum(numbers_input))
    while(1 not in numbers_input):
        numbers_input = for_no_ones(numbers_input)
        height += 1

# round 2https://www.youtube.com/playlist?list=PLzV8uWUcseN8x0c3q2hRx9X4vbLYSlipb
new_input = numbers_input[:]
new_height = 1
previousLine = reduct_the_first(new_input)
if([x==1 for x in previousLine] == [True for i in previousLine]):
    previousLine = []
    previousLine = previousLine.append(sum(previousLine))
    new_height += 1
    while(1 not in previousLine):
        previousLine = for_no_ones(previousLine)
        new_height +=1

if(new_height > height):
    height = new_height

print(str(depth) + ' ' + str(height))
