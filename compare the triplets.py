def compareTriplets(a,b):
    sa=0
    sb=0
    for i in range(0,3):
        if a[i]>b[i]:
            sa+=1
        elif a[i]<b[i]:
            sb+=1
    return [sa,sb];





a = list(map(int, input().rstrip().split()))
b= list(map(int, input().rstrip().split()))

print(compareTriplets(a,b));
