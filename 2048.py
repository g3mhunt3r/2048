def emp(T):
    for r in T:
        for c in r:
            if c==0:
                print(".",end = " ")
            else:
                print(c,end = " ")
        print()

T = [[1]*4]*4
emp(T)
