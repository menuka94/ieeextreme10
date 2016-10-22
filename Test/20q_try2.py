qs_and_lies = input()
no_of_qs = int(qs_and_lies[0])
no_of_lies = int(qs_and_lies[1])

balloons = [[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1]]

# take questions and answers as input

#case for single q and a
for i in range(no_of_qs):
    currentLine = input()
    questions = []
    answers = []
    probability = no_of_lies/no_of_qs

