t = int(input())
big_number = 1000

def equals_to_next(n):
    global sequence
    if (sequence[n] == sequence[n + 1]):
        return True


changes = 1

def get_next_occurrence(brush, i):
    global sequence, big_number
    x = [j for j, val in enumerate(sequence) if val == brush]
    big_number += 1000
    if(len(x) == 0):
        return big_number

    try:
        y = x[x.index(i) + 1]
        return y
    except ValueError:
        for k in x:
            if(k > i):
                return k
    except:
        return big_number


for i in range(t):
    N = int(input())
    sequence = input().split()
    # print(sequence)

    brush1 = sequence[0]
    brush2 = 0

    # case 1
    for i in range(0, len(sequence) - 2):
        print('s: ' + str(sequence))
        print('sequence i: ' + str(sequence[i]))
        print('sequence i+1: ' + str(sequence[i+1]))
        print('1: ' + str(brush1))
        print('2: ' + str(brush2))


        if (equals_to_next(i)):
            pass
        else:
            if (brush1 == sequence[i + 1] or brush2 == sequence[i + 1]):
                continue
            else:
                next_brush_1 = get_next_occurrence(brush1, i)
                next_brush_2 = get_next_occurrence(brush2, i)

                print('nb1: ' + str(next_brush_1))
                print('nb2: ' + str(next_brush_2))

                if (next_brush_1 > next_brush_2):
                    brush1 = sequence[i + 1]
                    changes += 1
                else:
                    brush2 = sequence[i + 1]
                    changes += 1

                print('# of changes at the end: ' + str(changes))


    print(changes)



