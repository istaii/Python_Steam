from random import *

n = randint(1, 100)
print('Добро пожаловать в угадайку')


def is_valid(x):
    if x in range(1, 101):
        return True
    else:
        return False


f = False
while f is False:
    t = int(input('Введите число от 1 до 100> '))
    f = is_valid(t)
    if f is False:
        print('А может быть все-таки введем целое число от 1 до 100?')
    else:
        if t < int(n):
            print('Ваше число меньше загаданного, попробуйте еще разок')
            f = False
        elif t > int(n):
            print('Ваше число больше загаданного, попробуйте еще разок')
            f = False
        else:
            print('Вы угадали! Поздравляем!')
            print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
            f = True
