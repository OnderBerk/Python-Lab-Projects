import time
def gcd(x, y):
    k = min(x, y)

    while k > 0:
        if(x % k == 0 and y % k == 0):
            return k;
        else:
            k=k-1

    return 1

x = int(input("Non-negative first integer >=2 : "))
y = int(input("Non-negative second integer >=2 : "))
start = time.time()

print("Greatest common divisor is:",gcd(x,y))
end = time.time()
print(end-start)
