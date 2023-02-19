import math

def generic(t, n, length, angle):
    '''
    Generic function for draws in turtle, used in geometric shapes below

    t: turtle
    n: number of line segments
    length: length of each segment
    angle: degrees between segments
    '''
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def polygon(t, n, length = 100):
    '''
    Draws a polygon with n sides

    t: turtle
    n: number of line segments
    length: length of each segment
    '''
    angle = 360 / n

    generic(t, n, length, angle)

def circle(t, r):
    '''
    Draws a circle with the given radius

    t: turtle
    r: radius
    '''
    circumference = 2 * math.pi * r
    n = int(circumference / 10) + 1
    length = circumference / n

    polygon(t, n, length)

def arc(t, r, angle):
    '''
    Draws an arc with the given radius and angle

    t: turtle
    r: radius
    angle: angle subtended by the arc, in degrees
    '''
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = float(angle) / n

    generic(t, n, step_length, step_angle)
