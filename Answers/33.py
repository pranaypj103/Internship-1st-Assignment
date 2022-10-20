for i in range(1,5):
    count=0
    for j in range(2*i):
        if j<(2*i)/2:
            count=count+1
            print(count,end=' ')
        else:
            print(count,end=' ')
            count=count-1
    print()