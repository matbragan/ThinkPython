def eval_loop():
    while True:
        a = input('what eval will analyze? ')
        a = str(a)
        if a == 'done':
            break
        try:
            print(eval(a))
        except:
            print('not possible')

eval_loop()