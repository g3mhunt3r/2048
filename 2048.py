def emp(T):
    for r in T:
        for c in r:
            if c==0:
                print(".",end = "\t")
            else:
                print(c,end = "\t")
        print("\n\n")

T = [[2048,2,4,8],[0]*4,[0]*4,[0]*4]
emp(T)
