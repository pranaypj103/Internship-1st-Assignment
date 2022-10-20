for i in range(1,6):
    count=0
    for j in range(0,2*i-1):
        if j<(2*i-1)/2:
            count=count+1
            print(count,end=' ')
        else:
            count=count-1
            print(count,end=' ')
    print()