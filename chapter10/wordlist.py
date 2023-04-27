import time

def append_word_list():
    start_time = time.time()
    word_list = []
    with open('../chapter9/words.txt') as file:
        for word in file:
            word_list.append(word)
    duration = time.time() - start_time
    return duration

def plus_word_list():
    start_time = time.time()
    word_list = []
    with open('../chapter9/words.txt') as file:
        for word in file:
            word_list = word_list + [word]
    duration = time.time() - start_time
    return duration

print('append_word_list duration - in seconds:', append_word_list())
print('plus_word_list   duration - in seconds:', plus_word_list())
