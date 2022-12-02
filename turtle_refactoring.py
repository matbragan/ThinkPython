import turtle
import math

def generic(n, length, angle):
    t = turtle.Turtle()

    for i in range(n):
        t.fd(length)
        t.lt(angle)

    turtle.mainloop()

def polygon(n, lenght):
    angle = 360 / n

    generic(n, lenght, angle)

def circle(r):
    circumference = 2 * math.pi * r
    n = int(circumference / 10) + 1
    length = circumference / n

    polygon(n, length)

def arc(r, angle):
    arc_length = (math.pi * r * angle) / 180
    n = int(arc_length / 10) + 1
    step_length = arc_length / n
    step_angle = angle / n

    generic(n, step_length, step_angle)

print('\n O que voce deseja desenhar?', end='\n\n')
print('[1] Poligono', end='\n')
print('[2] Circulo', end='\n')
print('[3] Arco', end='\n\n')
choice = int(input())

if choice == 1:
    print('\n Quantos lados terao seu poligono? ')
    n = int(input())
    print('Qual tamanho tera cada lado? ')
    length = int(input())

    polygon(n, length)

elif choice == 2:
    print('\n Qual sera o raio do seu circulo? ')
    r = int(input())

    circle(r)

elif choice == 3:
    print('\n Qual sera o raio do seu arco? ')
    r = int(input())
    print('Qual sera o angulo do seu arco? ')
    angle = int(input())

    arc(r, angle)

else:
    print('Escolha invalida')