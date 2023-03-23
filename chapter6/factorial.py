def factorial(n):
    '''
    Computes the factorial of n

    n: positive integer 
    '''
    if not isinstance(n, int):
        print('Factorial is only defined for integers.')
        return None
    elif n < 0:
        print('Factorial is not defined for negative integers.')
        return None
    else:
        # space = ' ' * (4*n)
        # print(space, 'factorial', n)
        result = n * factorial(n-1) if n > 0 else 1
        # print(space, 'returning', result)
        return result

if __name__ == '__main__':
    a = input('Enter a number for calculation your factorial ')

    try:
        a = int(a)
    except:
        pass

    print(factorial(a))
