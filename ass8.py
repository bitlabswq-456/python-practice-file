#8: Write a Python program to solve the Quadratic Equation
#Formula:
#ax2 + bx + c = 0, where
#a, b and c are real numbers and
#a ≠ 0

import cmath  
a = float(input('Enter a: '))  
b = float(input('Enter b: '))  
c = float(input('Enter c: '))  
  
# calculate the discriminant  
d = (b**2) - (4*a*c)  
sol = (-b-cmath.sqrt(d))/(2*a)  
print(sol)    