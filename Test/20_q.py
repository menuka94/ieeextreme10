#t = int(input())
#input()

balloons = [[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1]]

#------------------------------------------
# color_questions_and_separated = []
# color_questions_or_separated = []
# color_answers_and_separated = []
# color_answers_or_separated = []
# #------------------------------------------
# count_questions_and_separated = []
# count_questions_or_separated = []
# count_answers_and_separated = []
# count_answers_or_separated = []
#------------------------------------------

global_color_questions = []
global_color_answers = []

global_count_questions = []
global_count_answers = []

def determine():

    global global_color_questions, global_color_answers, global_count_questions, global_count_answers
    question_line = input()

    if(question_line[0:5] == 'color'):

        question_line = question_line.replace('color ', '')
        color_questions_and = ['and']
        color_questions_or = ['or']
        color_answers_and = []
        color_answers_or = []

        if(question_line.find('and') != -1):
            print('COLOR AND')
            color_questions_and.append(question_line.split('and'))
            color_answers_and.append(input())

            global_color_questions.append(color_answers_and)
            global_color_answers.append(color_answers_and)

        elif(question_line.find('or') != -1):
            print('COLOR OR')
            color_questions_or.append(question_line.split('or'))
            color_answers_or.append(input())

            global_color_questions.append(color_questions_or)
            global_color_answers.append(color_answers_or)
        else:
            print('COLOR JUST')
            color_questions_and.append(question_line)
            print('temp Q: ' + str(color_questions_and))
            color_answers_and.append(input())

            global_color_questions.append(color_answers_and)
            global_color_answers.append(color_answers_and)


    elif(question_line[0:5] == 'count'):
        question_line = question_line.replace('count ', '')
        count_questions_and = ['and']
        count_questions_or = ['or']
        count_answers_and = []
        count_answers_or = []

        if(question_line.find('and') != -1):
            print('COUNT AND')
            count_questions_and.append(question_line.split('and'))
            count_answers_and.append(input())

            print('1: ' + str(count_questions_and))
            print('2: ' + str(count_answers_and))

            global_count_questions.append(count_questions_and)
            global_count_answers.append(count_answers_and)

        elif (question_line.find('or') != -1):
            print('COUNT OR')
            count_questions_or.append(question_line.split('or'))
            count_answers_or.append(input())

            global_count_questions.append(count_questions_or)
            global_count_answers.append(count_answers_or)

        else:
            print('COUNT JUST')
            count_questions_and.append(question_line)
            count_questions_and.append(input())

            global_count_questions.append(count_questions_and)
            global_count_answers.append(count_answers_and)

        print('\n')

def check_probability(questions, lies):
    probability = lies / questions
    return probability

def test():
    global global_color_questions, lies

# main program
for cases in range(1):
    qs_and_lies = input().split()
    qs = int(qs_and_lies[0])
    lies = int(qs_and_lies[1])

    # print("No. of q s: " + str(qs))
    # print("No. of lies: " + str(lies))

    for i in range(qs):
        determine()

    print("Count Questions: " + str(global_count_questions))
    print("Count Answers: " + str(global_count_answers))

    print("Color Questions: " + str(global_count_questions))
    print("Color Answers: " + str(global_color_answers))

