for i in range(1,6):
    for j in range(1,5):
        if i==1 or i==int(5/2+1):
            print('@',end=' ')
        elif(j==1 or j==4):
            print('@',end=' ')
        else:
            print(' ',end=' ')
    print()