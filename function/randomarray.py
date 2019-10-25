import random
def randomarray(n):
    a = []
    for i in range(n):
        a.append(random.random())
    return a

b = randomarray(10)
for i in b : print(i)
