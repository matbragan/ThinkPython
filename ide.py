def square(a, x):
    while True:
        print(x)
        y = (x + a/x) / 2
        if x == y:
            break
        x = y

square(25, 98)