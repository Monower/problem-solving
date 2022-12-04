"""In this program three side of a triangle is taken from the user.
 Then by using herons formula area, A=s(s-a)(s-b)(s-c)**.5
 Where s= (a+b+c)/2"""

a = float(input("enter the first side of the triangle: "));
b = float(input("enter the second side of the triangle: "));
c = float(input("enter the third side of the triangle: "));

s = (a+b+c)/2;
a = s*(s-a)*(s-b)*(s-c);

print("The are of the triangle is : {:.3f}".format(s));