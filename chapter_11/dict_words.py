d = dict()
with open('../chapter9/words.txt') as file:
    for a in file:
        d[a] = 1

print(d)
