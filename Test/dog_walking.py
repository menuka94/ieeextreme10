#  sum of ranges of the groups is minimized
cases = int(input())
for eachCase in range(cases):
    N_and_K = input().split(' ')
    N = int(N_and_K[0])
    K = int(N_and_K[1])
    dogs = []
    for dog in range(N):
        dogs.append(int(input()))

    print("\n---Printing Input")
    print(str(N) + " " + str(K))
    for eachDog in dogs:
        print(eachDog)
