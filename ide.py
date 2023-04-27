def histogram(s):
    d = dict()
    s = s.lower()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

def find_index_of_value(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise LookupError('value does not appear in the dictionary')

def invert_dict(d):
    inverse = dict()
    for k in d:
        val = d[k]
        if val not in inverse:
            inverse[val] = [k]
        else:
            inverse[val].append(k)
    return inverse

h = histogram('Paralelepipedo')

print(h)
print(invert_dict(h))