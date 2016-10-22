def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]

secondLine = input().split()
number_of_entries = secondLine[0]
per_group = int(secondLine[1])

secondLine = secondLine[2:]

table = [0,0,1.88,1.023,0.729,0.577,0.483,0.419,0.373,0.337,0.308]


# getting into groups of 'per_group'
data = list(chunks(secondLine, per_group))

for d in range(len(data)):
    data[d] = [int(x) for x in data[d]]

averages = []
ranges = []

print("I'm here: " + str(data))

for d in data:
    averages.append(float(sum(d))/float(len(d)))
    ranges.append(max(d) - min(d))

i = 0
while i < len(data):
    print(data[i])
    print(averages[i])
    print(ranges[i])
    print('\n--------------')
    i += 1

grand_average = round(float(sum(averages))/float(len(averages)),2)
range_average = float(sum(ranges))/float(len(ranges))

print("Grand Average: " + str(grand_average))
print("Range Average: " + str(range_average))

UCL = grand_average + table[per_group]*range_average
LCL = grand_average - table[per_group]*range_average
CL = grand_average

SIGMA = (UCL-LCL)/float(6)

print("UCL: " + str(UCL))
print("LCL: " + str(LCL))
print("CL: " + str(CL))
print("SIGMA: " + str(SIGMA))

out_of_control = False

for n in secondLine:
    if(abs(int(n)-grand_average) > 3 * SIGMA):
        out_of_control = True

for i in range(len(secondLine)-2):
    value = 2*SIGMA
    if(abs(secondLine[i] - grand_average) > value):
        if(abs(secondLine[i+1] - grand_average) > value):
            out_of_control = True

    elif (abs(secondLine[i] - grand_average) > value):
        if (abs(secondLine[i + 2] - grand_average) > value):
            out_of_control = True

    elif (abs(secondLine[i+1] - grand_average) > value):
        if (abs(secondLine[i + 2] - grand_average) > value):
            out_of_control = True


for i in range((len(secondLine)-4)):
    five_values = []
    five_values.extend(secondLine[i:i+5])
    five_values = sorted(five_values)
    if(five_values[1] > SIGMA + grand_average):
        out_of_control = True

for i in range(len(secondLine) - 7):
    eight_values = []
    eight_values.extend(secondLine[i:i+8])



if(out_of_control):
    print("Out of control")