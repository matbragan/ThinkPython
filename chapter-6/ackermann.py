def ack(m, n):
    '''
    Computes the Ackermann function A(m, n)
    
    See http://en.wikipedia.org/wiki/Ackermann_function
    
    n, m: non-negative integers
    '''
    cond = (
        not isinstance(m, int) or
        not isinstance(n, int) or
        m < 0 or
        n < 0
    )
    if cond:
        print('Both numbers need be positive integers.')
        return None
    
    elif m == 0:
        return n + 1
    elif n == 0:
        return ack(m-1, 1)
    return ack(m-1, ack(m, n-1))

print(ack(0, 3))