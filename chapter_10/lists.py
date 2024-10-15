def nested_sum(t):
    total = 0
    for i in range(len(t)):
        total += sum(t[i])
    return total

def cumsum(t):
    t2 = []
    for i in range(len(t)):
        t2.append(sum(t[:i+1]))
    return t2

def middle(t):
    return t[1:-1]

def chop(t):
    del t[0]
    del t[-1]

def is_sorted(t):
    return t == sorted(t)

def is_anagram(a, b):
    if len(a) != len(b): return False
    t = list(b)
    for i in a:
        if i not in t:
            return False
        del t[t.index(i)]
    return True

def has_duplicates(t):
    t2 = t
    for i in t:
        del t2[t2.index(i)]
        if i in t2:
            return True
    return False

if __name__ == '__main__':
    print(has_duplicates([1, 5, 45, 1]))