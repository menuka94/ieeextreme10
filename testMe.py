def reduct_the_first(numbers):
    numbers_input = numbers[:]
    if(numbers_input[0] > 1):
        numbers_input[0] -= 1
        numbers_input.insert(0, 1)

    return numbers_input


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


numbers = [int(n) for n in input().split()]

# # print(reduct_the_first(numbers))
# print("For No 1s: " + str(for_no_ones(numbers)))
# print("For 1s in the middle: " + str(ones_in_the_middle(numbers)))
# print("Reduct the first: " + str(reduct_the_first(numbers)))

class Tree():
    height = 0
    def __init__(self):
        global height
        self.no_1_s = None
        self.ones_in_middle = None
        self.reduct_first = None
        self.value = None
        self.height += 1


root = Tree()
root.value = numbers[:]
root.no_1_s = for_no_ones(root.value[:])
root.ones_in_middle = ones_in_the_middle(root.value[:])
root.reduct_first = reduct_the_first(root.value[:])
print(Tree.height)

