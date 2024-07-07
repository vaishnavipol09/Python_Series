#import math

#def calculate_area_circle(radius):
#    return math.pi * radius ** 2
#print(calculate_area_circle(9))


import math
def calculate_radius(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference
a , c = calculate_radius(9)
print("\n Area of circle: ", a)
print("\n Circumference of circle: ", c)
print("\n")