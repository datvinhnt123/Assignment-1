import random
def pi():
    i=int(input("Enter a number of random points: "))
    n=0
    for e in range(i):
        x=random.random()
        y=random.random()
        if x**2+y**2<1:
            n=n+1
    pi=4*n/i
    return pi
print(pi())