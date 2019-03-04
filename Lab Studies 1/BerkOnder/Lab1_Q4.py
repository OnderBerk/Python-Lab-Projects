import math


def sieve(Number):
    sqr = math.sqrt(Number)

    x = []
    r = []

    for k in range(Number + 1):
        x.append(k)

    x[1] = 0

    for i in range(2,math.floor(sqr)):
        for s in range(i+1, Number + 1):
            if x[s] % i == 0:
                x[s] = 0

    for i in range(Number):
        if(x[i] != 0):
            r.append(x[i])

    return r

def Prime(x):
    liste = sieve(x)
    i = 0
    r = []
    while x != 1 and i < len(liste):
        while(x % liste[i] == 0):
            x /= liste[i]
            r.append(liste[i])
        i+=1
    return r

def Gcd(x, y):
    mx = Prime(x)
    my = Prime(y)


    result = 1
    r = []

    if(len(mx) <= len(my)):
        for k in range(len(mx)):
            if(mx[k] in my):
                result *= mx[k]
                r.append(mx[k])
    else:
        for k in range(len(my)):
            if(my[k] in mx):
                result *= my[k]
                r.append(my[k])

    if(result==1):
        return 1,[]
    else:
        return result, r




m = int(input("Non-negative integer >=2 please: "))
n = int(input("Another Non-negative integer >=2 please: "))

result, r = Gcd(m,n)

print(f"Common prime factors are: {r}")
print(f"Greatest common divisor: {result}")

