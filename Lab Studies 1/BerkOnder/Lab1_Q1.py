import random
def mat(x):
    for k in range(x):
        for z in range(x):
            randomm = random.randint(0, 1)
            print("", randomm, end="")
        print("\n", end="")

x = int(input("Please enter an integer !!"))
mat(x)
