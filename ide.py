def countdown(n):
    while n > 0:
        print(n)
        n = n - 1

# countdown(10)

def print_n(s, n):
    if n <= 0:
        return
    print(s)
    print_n(s, n-1)

def print_m(s, m):
    while m > 0:
        print(s)
        m = m - 1

print_n('oi', 4)

print('------------------')

print_m('oi', 4)