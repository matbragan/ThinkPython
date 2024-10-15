from random import randint
from lists import has_duplicates

def birthday_list(n):
    t = []
    for i in range(n):
        t.append(randint(1, 365))
    return t

def count_matches(n_students, n_simulations):
    count = 0
    for i in range(n_simulations):
        t = birthday_list(n_students)
        if has_duplicates(t):
            count += 1
    return count

def main():
    n_students = 23
    n_simulations = 1000
    count = count_matches(n_students, n_simulations)
    print(f'{n_simulations} simulations with {n_students} students had {count} matches')

if __name__ == '__main__':
    main()