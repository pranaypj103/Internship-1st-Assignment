for i in range(1,8):
    for j in range(1,10):
        if (i==1 or i==7):
            print('*',end=' ')
        elif(j==int(9/2+1)):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()