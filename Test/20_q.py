t = int(input())

balloons = [[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1]]

for cases in range(t):
    input()
    qs_and_lies = input().split()
    qs = int(qs_and_lies[0])
    lies = int(qs_and_lies[1])

    questions = []
    answers = []

    for q in range(qs):
        questions.append()


# not determined whether true or false
colors = []
counts = []

def determine():
    global colors, counts
    question_line = input()

    first_word = question_line.split()[0]
    if(first_word == 'color'):
        question_line.replace('color ', '')
        color_questions_and_separated = ['and']
        color_questions_or_separated = ['or']
        color_answers_and_separated = []
        color_answers_or_separated = []

        if(question_line.find('and')):
            color_questions_and_separated.append(question_line.split('and'))
            color_answers_and_separated.append(input())

        elif(question_line.find('or')):
            color_questions_or_separated.append(question_line.split('or'))
            color_answers_or_separated.append(input())
        else:
            color_questions_and_separated.append(question_line.strip())
            color_answers_and_separated.append(input())


    elif(first_word == 'count'):
        question_line.replace('count ', '')
        count_questions_and_separated = ['and']
        count_questions_or_separated = ['or']
        count_answers_and_separated = []
        count_answers_or_separated = []

        if(question_line.find('and')):
            count_questions_and_separated.append(question_line.split('and'))
            count_answers_and_separated.append(input())
        elif (question_line.find('or')):
            count_questions_or_separated.append(question_line.split('or'))
            count_answers_or_separated.append(input())
        else:
            count_questions_and_separated.append(question_line.strip())
            count_questions_and_separated.append(input())






