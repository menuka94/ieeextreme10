N = int(input())
sequence = input().split()
print(sequence)

brush1 = sequence[0]
brush2 = 0

def equals_to_next(n):
    global sequence
    if(sequence[n] == sequence[n+1]):
        return True

changes = 1

def get_next_occurrence(brush, i):
    global sequence
    x = [j for j,val in enumerate(sequence) if val==brush]

    try:
        y = x[x.index(i)+1]
        return y
    except:
        return 1000


#case 1
for i in range(1, len(sequence)-2):
    if(equals_to_next(i+1)):
        pass
    else:
        if(brush1 == sequence[i+1] or brush2 == sequence[i+1]):
            continue
        else:
            next_brush_1 = get_next_occurrence(brush1, i)
            next_brush_2 = get_next_occurrence(brush2, i)

            if(next_brush_1 > next_brush_2):
                brush1 = sequence[i+1]
                changes += 1
            else:
                brush2 = sequence[i+1]
                changes += 1

        # brush2 = sequence[i+1]
        # changes += 1

print(changes)




