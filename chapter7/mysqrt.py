import math

def mysqrt(a):
    x = a/2
    epsilon = 0.0000000001
    while True:
        y = (x + a/x) / 2
        if abs(y - x) < epsilon:
            return y
        x = y

print("a   mysqrt(a)     math.sqrt(a) diff")
print("-   ---------     ------------ ----")

a = 1
while a < 10:
    diff = math.sqrt(a)-mysqrt(a)
    print('{0:.1f} {1:.11f} {2:.10f} {3}'.format(a, mysqrt(a), math.sqrt(a), diff))
    a += 1