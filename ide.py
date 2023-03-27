def in_both(word1, word2):
    for l in word1:
        if l in word2:
            print(l)

in_both('Pinguito', 'Pantera')

print(' Pinguito'.strip('toi'))