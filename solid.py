import math
from .flat import circle_area

def sphere_volume(r):
    return 4 / 3 * math.pi * r ** 3

def cube_volume(a):
    return a ** 3

def hemisphere_area(r):
    return 2 * math.pi * r ** 2 + circle_area(r)
