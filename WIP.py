def collapse(c):
    lnv=-1
    lnp=-1
    ls=-1
    for i in range(4):
        #print("i: "+str(i)+" lnv: "+str(lnv)+" lnp: "+str(lnp)+" ls: "+str(ls))
        #print(c)
        if c[i]==0 and ls==-1: # If number is 0 and you haven't seen a zero before
            ls=i
        elif c[i]!=0: # If number not zero, do this
            if c[i]==lnv: # Check if same number was last seen for collapse
                c[lnp]=lnv*2 # double prev
                c[i]=0 # clear current
                lnv=-1 # reset last seen val
                ls=lnp+1 # set space to next block
                lnp=-1 # reset last seen pos
                continue
            else: # If new number not same as old
            #elif lnp!=-1: # Won't go in here if last pair just collapsed
                if ls==-1: # If no space before
                    lnv=c[i] # this is now the last seen number
                    lnp=i
                    continue
                else: # If there was a space before
                    c[ls]=c[i] # put this number into last space
                    lnv=c[i] # remember that number as last seen number
                    lnp=ls # remember its new position
                    c[i]=0 # empty its current position
                    ls=lnp+1 # set the space after that to be the fist empty space
                    continue
            # Only here if number not zero AND If new number not same as old AND If there was a space before
            # Only here if number not zero AND If new number not same as old AND If there was a space before
            lnv=c[i]
            lnp=i
