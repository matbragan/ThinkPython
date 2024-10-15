fin = open('words.txt')

def twenty_letters_more():
    for line in fin:
        word = line.strip()
        if len(word) > 20:
            print(word)

def has_no_e():
    total = 0
    no_e = 0
    for line in fin:
        word = line.strip()
        total += 1
        if 'e' not in word:
            print(word)
            no_e +=  1
    print(no_e/total*100)

def avoids(word, forbidden):
    for letter in word:
        if letter in forbidden:
            return False
    return True


print(avoids('Matheus', ['g', 'a']))