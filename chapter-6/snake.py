import time

def snake(n=0, count=0):
    '''
    Creation of a snake, using spaces and imagination
    '''
    space = ' ' * (4*n)
    stop = 10
    if count == stop:
        return
    elif n <= 5:
        print(space, 'shhh')
        time.sleep(2)
        snake(n+1, count+1)
    elif n >= 0:
        print(space, 'shhh')
        time.sleep(2)
        snake(n-1, count+1)

snake()