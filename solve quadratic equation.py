"""This program computes roots of a quadratic equation when coefficients a, b and c are known.
The standard form of a quadratic equation is:

ax2 + bx + c = 0, where
a, b and c are real numbers and
a ≠ 0

The solutions of this quadratic equation is given by:

(-b ± (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
"""

import math

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))


d= math.sqrt(b)-4*(a*b);

sol1= (-b + (math.sqrt(b) - 4*(a*c)))/(2*a)
sol2= (-b - (math.sqrt(b) - 4*(a*c)))/(2*a)

print("The solutions are {} and {}.".format(sol1,sol2));
