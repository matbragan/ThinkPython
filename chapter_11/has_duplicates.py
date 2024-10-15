def has_duplicates(t):
    d = {}
    for x in t:
        if x in d:
            return True
        d[x] = True
    return False

if __name__ == '__main__':
    l = [1, 5, 45, 1]
    print(has_duplicates(l))