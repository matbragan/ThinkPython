def first(word):
    '''returns the first letter of the word'''
    return word[0]

def last(word):
    '''returns the last letter of the word'''
    return word[-1]

def middle(word):
    '''returns the middle letters of the word'''
    return word[1:-1]

def is_palindrome(word):
    '''function to analyze if a word is a palindrome'''
    if first(word) != last(word):
        return False
    if len(word) >= 3:
        return is_palindrome(middle(word))
    return True
    

word = 'subinoonibus'

print(is_palindrome(word))