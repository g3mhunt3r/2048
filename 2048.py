import random

def emp(T):
    for r in T:
        for c in r:
            if c==0:
                print(".",end = "\t")
            else:
                print(c,end = "\t")
        print("\n\n")

def add(T,n=2):
    while True:
        x=random.randint(0,3)
        y=random.randint(0,3)
        if T[x][y]==0:
            T[x][y]=n
            break

def collapseLR(T,dir):
    for j in range(4):
        lnv=-1
        lnp=-1
        ls=-1
        if dir=='a':
            x=range(4)
        elif dir=='d':
            x=range(3,-1,-1)
        for i in x:
            #print("i: "+str(i)+" lnv: "+str(lnv)+" lnp: "+str(lnp)+" ls: "+str(ls))
            #print(c)
            if T[j][i]==0 and ls==-1: # If number is 0 and you haven't seen a zero before
                ls=i
            elif T[j][i]!=0: # If number not zero, do this
                if T[j][i]==lnv: # Check if same number was last seen for collapse
                    T[j][lnp]=lnv*2 # double prev
                    T[j][i]=0 # clear current
                    lnv=-1 # reset last seen val
                    if dir=='a':
                        ls=lnp+1 # set space to next block
                    elif dir=='d':
                        ls=lnp-1 #set space to previous block
                    lnp=-1 # reset last seen pos
                    continue
                else: # If new number not same as old
                #elif lnp!=-1: # Won't go in here if last pair just collapsed
                    if ls==-1: # If no space before
                        lnv=T[j][i] # this is now the last seen number
                        lnp=i
                        continue
                    else: # If there was a space before
                        T[j][ls]=T[j][i] # put this number into last space
                        lnv=T[j][i] # remember that number as last seen number
                        lnp=ls # remember its new position
                        T[j][i]=0 # empty its current position
                        if dir=='a':
                            ls=lnp+1 # set the space after that to be the fist empty space
                        elif dir=='d':
                            ls=lnp-1 # set the space before that to be the first empty space
                        continue
                # Only here if number not zero AND If new number not same as old AND If there was a space before
                # Only here if number not zero AND If new number not same as old AND If there was a space before
                lnv=T[j][i]
                lnp=i

def transpose(T):
    for i in range(3):
        for j in range(3,i,-1):
            t=T[i][j]
            T[i][j]=T[j][i]
            T[j][i]=t

def collapse(T,dir):
    if dir=='a' or dir=='d':
        collapseLR(T,dir)
    elif dir=='w':
        dir='a'
        transpose(T)
        collapseLR(T,dir)
        transpose(T)
    elif dir=='s':
        dir='d'
        transpose(T)
        collapseLR(T,dir)
        transpose(T)

def checkzero(T):
    for i in range(4):
        for j in range(4):
            if T[i][j]==0:
                return True
    return False

T=[[0]*4,[0]*4,[0]*4,[0]*4]
add(T,4)
add(T)
emp(T)
while True:
    dir = input("Enter direction to collapse: ")
    collapse(T,dir)
    if checkzero(T) == False:
        print("Game Over\nEnter q to exit, r to restart: ")
        c=input()
        if c=='q':
            break
        elif c=='r':
            T=[[0]*4,[0]*4,[0]*4,[0]*4]
            add(T,4)
    add(T)
    emp(T)
