"""Python Program to Find the Factorial of a Number
"""

n = int(input("enter the number to find factorial: "));

factorial =1;

if n<0: print("there is no factorial for negative number.");
elif n==0: print("factorial of 0 is 1.");
else:
    for i in range(1,n+1):
        factorial= factorial*i;
    print(factorial);




