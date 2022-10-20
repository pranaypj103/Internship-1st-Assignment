for i in range(1,10):
    for j in range(1,13):
        if i==1:
            if j<=7:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        elif(i==9):
            if j<=6:
                print(' ',end=' ')
            else:
                print('*',end=' ')
        elif(i==5):
            print('*',end=' ')
        elif(i<=4):
            if j==7 or j==12:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        else:
            if j==1 or j==7:
                print('*',end=' ')
            else:
                print(' ',end=' ')
    print()