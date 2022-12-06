"""Python Program to Check Leap Year
"""
n = int(input("enter a the year: "))

if n%400==0 and n%100==0:
    print("{} is a leap year.".format(n));
elif n%4==0 and n%100 !=0:
    print("{} is a leap year.".format(n));
else: print("{} is not a leap year.".format(n));




