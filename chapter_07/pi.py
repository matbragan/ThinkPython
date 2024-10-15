import sys
sys.path.append('../chapter6')

from factorial import factorial
import math

def estimate_pi():
    '''function to estimate pi, based in Srinivasa Ramanujan formula'''
    k = 0
    addition = 0
    while True:
        numerator = (factorial(4*k)) * (1103 + 26390*k)
        denominator = (factorial(k)**4) * (396**(4*k))
        term = numerator/denominator
        addition += term
        
        if abs(term) < 1e-15:
            break
        k += 1
    
    factor = 2*math.sqrt(2) / 9801
    result = factor * addition
    return 1/result

if __name__ == '__main__':
    print(f'my   estimate pi - {estimate_pi()}')
    print(f'math estimate pi - {math.pi}')
