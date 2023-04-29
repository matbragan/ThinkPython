def histogram(s):
    d = dict()
    s = s.lower()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

# def invert_dict(d):
#     inverse = {}
#     for key in d:
        

h = histogram('Pinguito & Pantera')
print(h)
print(invert_dict(h))