import random

def emp(T):
    for r in T:
        for c in r:
            if c==0:
                print(".",end = "\t")
            else:
                print(c,end = "\t")
        print("\n\n")

def add(T):
    while True:
        x=random.randint(0,3)
        y=random.randint(0,3)
        if T[x][y]==0:
            T[x][y]=2
            break

T = [[2048,2,4,8],[0]*4,[0]*4,[0]*4]
emp(T)
add(T)
emp(T)
