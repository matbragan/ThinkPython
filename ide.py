def letters(string):
    for l in string:
        print(l)

def invert_letters(string):
    i = 1
    while i <= len(string):
        letter = string[-i]
        print(letter)
        i += 1

def ducklings():
    prefixes = 'JKLMNOPQ'
    suffix = 'ack'

    for l in prefixes:
        print(l + suffix) if l not in ['O', 'Q'] else print(l + 'u' + suffix)

print('banana'[:])