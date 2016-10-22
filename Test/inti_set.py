from math import sqrt

def isPrime(n):
    sqrt_of_n = int(sqrt(n)) + 1
    if(n == 1):
        return False
    if(n == 2):
        return True
    if(n%2 == 0):
        return False
    else:
        for i in range(3, sqrt_of_n):
            if(n%i == 0):
                return False

    return True

for i in range(1, 100):
    if(isPrime(i)):
        print(i)

def get_inti_set(N, A, B):
    inti_set = []
    for i in range(A, B+1):
        if(isPrime(i)):
            inti_set.append(i)
