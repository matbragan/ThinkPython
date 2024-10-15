def find_index_of_value(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise LookupError('value does not appear in the dictionary')

d = {'a': 4, 'b': 6, 'c': 8}

print(find_index_of_value(d, 2))