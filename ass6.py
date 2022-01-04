#6. Write a Python program to calculate the Area of a Triangle
#Formula:
#If a, b and c are three sides of a triangle. Then, s = (a+b+c)/2
#area = √(s(s-a)*(s-b)*(s-c))

a = float(input('Enter first side: '))
b = float(input('Enter second side: '))
c = float(input('Enter third side: '))

# calculate the semi-perimeter
s = (a + b + c) / 2

# calculate the area
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print(area)
