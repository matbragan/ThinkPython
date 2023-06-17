def histogram(s):
    d = dict()
    s = s.lower()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

def invert_dict(d):
    inverse = dict()
    for k in d:
        val = d[k]
        if val not in inverse:
            inverse[val] = [k]
        else:
            inverse[val].append(k)
    return inverse

def invert_dict2(d):
    inverse = dict()
    for k in d:
        val = d[k]
        inverse.setdefault(val, []).append(k)
    return inverse

if __name__ == '__main__':

    h = histogram('Paralelepipedo')

    print(h)
    print(invert_dict(h))
    print(invert_dict2(h))