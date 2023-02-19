import turtle

from polygon import polygon, circle, arc
from flower import flower, move

print('What do you want to draw?\n')
print('[1] A Polygon', end='\n')
print('[2] A Circle', end='\n')
print('[3] An Arc', end='\n')
print('[4] Three Different Flowers\n')
choice = int(input())

if choice == 1:
    n = int(input('How many sides will your polygon have? '))

    t = turtle.Turtle()
    polygon(t, n)

    # wait for the user to close the window
    turtle.mainloop()

elif choice == 2:
    r = int(input('What will be the radius of your circle? '))

    t = turtle.Turtle()
    circle(t, r)

    # wait for the user to close the window
    turtle.mainloop()

elif choice == 3:
    r = int(input('What will be the radius of your arc? '))
    angle = int(input('What will be the angle, in degrees, of your arc? '))

    t = turtle.Turtle()
    arc(t, r, angle)

    # wait for the user to close the window
    turtle.mainloop()

elif choice == 4:
    t = turtle.Turtle()

    move(t, -100)
    flower(t, 7, 60.0, 60.0)

    move(t, 100)
    flower(t, 10, 40.0, 80.0)

    move(t, 100)
    flower(t, 20, 140.0, 20.0)

    t.hideturtle()
    # wait for the user to close the window
    turtle.mainloop()

else:
    print('Escolha invalida')