numbers_input_2 = [2,1,1] # <= [3,1] <= [2,2] <= [2,1,1]
                        # <= [3,1] <= [1,2,1]
                        # <= [1,1,1,1] <= [4] <= [1,3]
numbers_input = [3,4] # <= [2,2,3] <= [3,1,1,2] <= [1,2,1,1,2]
                        # <= [1,2,4]

# Case I - Reduct 1 from the first element and insert 1 at the beginning
def reduct_the_first(numbers):
    numbers_input = numbers
    if(numbers_input[0] > 1):
        numbers_input[0] -= 1
        numbers_input.insert(0, 1)

    return numbers_input

# Case II - no 1's in the list

lists = [numbers_input[:]] # insert a copy into the list

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

# if no 1's present
while lists[-1][0] != 1 and (1 not in lists[-1]):
    previousLine = for_no_ones(lists[-1])
    lists.append(previousLine[:])

# for 1's in the middle
while lists[-1][0] != 1:
    previousLine = ones_in_the_middle(numbers_input)
    lists.append(previousLine[:])

# last method call - until the first number becomes 1
while lists[-1][0] != 1:
    previousLine = reduct_the_first(lists[-1])

for eachList in lists:
    print(eachList)
