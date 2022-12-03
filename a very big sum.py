def aVeryBigSum(arr):
    sum=0;
    for i in range(len(arr)):
        sum=sum+arr[i];
    return sum;






arr = list(map(int, input().rstrip().split()))

print(aVeryBigSum(arr));


