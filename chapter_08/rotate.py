def rotate_word(word, n):
    '''
    Rotates a word in n places

    word: string
    n: integer

    Returns: string
    '''
    rotate_word = ''
    for a in word:
        ord_b = n + ord(a)
        b = chr(ord_b)
        rotate_word += b

    return rotate_word

if __name__ == '__main__':
    for i in range(10):
        print(f'Rotate {i} of Milena - {rotate_word("Milena", i)}')
    for i in range(10):
        print(f'Rotate {i} of Matheus - {rotate_word("Matheus", i)}')
    for i in range(10):
        print(f'Rotate {i} of Bela - {rotate_word("Bela", i)}')    