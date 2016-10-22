def determine():
    question_line = input()

    if(question_line[0:5] == 'color'):
        question_line = question_line.replace('color ', '')
        color_questions_and_separated = ['and']
        color_questions_or_separated = ['or']
        color_answers_and_separated = []
        color_answers_or_separated = []

        if(question_line.find('and') != -1):
            color_questions_and_separated.append(question_line.split('and'))
            color_answers_and_separated.append(input())

        elif(question_line.find('or') != -1):
            color_questions_or_separated.append(question_line.split('or'))
            color_answers_or_separated.append(input())
        else:
            color_questions_and_separated.append(question_line.strip())
            color_answers_and_separated.append(input())

        print('\n')
        print("Color-and-Q: " + str(color_questions_and_separated))
        print("Color-and-A: " + str(color_answers_and_separated))
        print('---------------------------------------------')
        print("Color-or-Q: " + str(color_questions_or_separated))
        print("Color-or-A: " + str(color_answers_or_separated))


    elif(question_line[0:5] == 'count'):
        question_line = question_line.replace('count ', '')
        count_questions_and_separated = ['and']
        count_questions_or_separated = ['or']
        count_answers_and_separated = []
        count_answers_or_separated = []

        if(question_line.find('and') != -1):
            count_questions_and_separated.append(question_line.split('and'))
            count_answers_and_separated.append(input())
        elif (question_line.find('or') != -1):
            count_questions_or_separated.append(question_line.split('or'))
            count_answers_or_separated.append(input())
        else:
            count_questions_and_separated.append(question_line.strip())
            count_questions_and_separated.append(input())

        print('\n')

        print("Count-and-Q: " + str(count_questions_and_separated))
        print("Count-and-A: " + str(count_answers_and_separated))
        print('-------------------------------------------')
        print("Count-or-Q: " + str(count_questions_or_separated))
        print("Count-or-A: " + str(count_answers_or_separated))


determine()
