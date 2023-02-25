import math

def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    result = math.sqrt(dsquared)
    return result

# print(distance(1, 2, 4, 6))

def is_between(x, y, z):
    return x <= y <= z

# print(is_between(3, 2, 3))

def factorial(n):
    return n * factorial(n-1) if n > 0 else 1

print(factorial(0))