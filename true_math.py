from math import inf
def divide(first, second):
    # first = int(input('Укажите делимое: '))
    # second = int(input('Укажите делитель: '))
    if second == 0:
        division = inf
    else:
        division = first / second
    return division
