def collapse(T):
    for j in range(4):
        lnv=-1
        lnp=-1
        ls=-1
        for i in range(4):
            #print("i: "+str(i)+" lnv: "+str(lnv)+" lnp: "+str(lnp)+" ls: "+str(ls))
            #print(c)
            if T[j][i]==0 and ls==-1: # If number is 0 and you haven't seen a zero before
                ls=i
            elif T[j][i]!=0: # If number not zero, do this
                if T[j][i]==lnv: # Check if same number was last seen for collapse
                    T[j][lnp]=lnv*2 # double prev
                    T[j][i]=0 # clear current
                    lnv=-1 # reset last seen val
                    ls=lnp+1 # set space to next block
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
                        ls=lnp+1 # set the space after that to be the fist empty space
                        continue
                # Only here if number not zero AND If new number not same as old AND If there was a space before
                # Only here if number not zero AND If new number not same as old AND If there was a space before
                lnv=T[j][i]
                lnp=i
