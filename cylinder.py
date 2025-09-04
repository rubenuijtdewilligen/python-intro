import math

def create_cylinder(radius, height):
    area = math.pi * math.pow(radius, 2)
    circumference = 2 * math.pi * radius
    volume = area * height
    surface = circumference * height
    return volume, surface

r = float(input("Enter radius: "))
h = float(input("Enter radius: "))

print(create_cylinder(r, h))