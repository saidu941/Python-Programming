#2.Write a python program to
#a.Take radius of a circle as input from user and calculate area , circumference and print it.
#b.Check whether a number input by the user is even or odd

import math
radius = int(input('enter radius of the circle'))
area = math.pi*radius* radius
circum=2*math.pi*radius
print('area is : ',area)
print('circumference is : ',circum)
