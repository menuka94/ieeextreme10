def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)

    print('Factors: ' + str(factors))
    return factors

def problem(n):
    return [x for x in range(1, n + 1) if n % x == 0]


t = int(input())
while (t >= 1):
    lst = list(map(int, input().split()))
    n = lst[0]
    a = lst[1]
    b = lst[2]
    seq = []
    pfac = prime_factors(n)
    fac = problem(n)
    i = a
    while(i < b+1):
        flag = False
        if (i not in pfac):
            el = 0
            while(el < len(pfac)):
                if(i%pfac[el] == 0):
                    flag = True
                    break
                el += 1

            if (flag == False):
                seq.append(i)
        i += 1

    tot = 0


    x = 0
    while(x < len(seq)):
        if(seq[x] >= a and seq[x] <= b):
            tot += seq[x]
        x += 1

    print(tot % 1000000007)

    t -= 1