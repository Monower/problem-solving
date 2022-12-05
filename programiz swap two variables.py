"""Python Program to Swap Two Variables
"""

#with a temporary variable
'''a,b = 1,2;

temp  = a;
a=b;
b=temp;

print("After sqapping the variables are {} and {}".format(a,b));'''

#without a temporary variable

a,b=1,2;
a,b=b,a;

print("After sqapping the variables are {} and {}".format(a,b));


