from math import *


def getParametrs():
    print('Эта программа считает корни уравнения по значениям a, b, c')
    print('Ссылка на алгоритм: https://ru.wikipedia.org/wiki/Формула_Кардано/')
    print('y = ax³ + bx² + cx + d')
    parametrs = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
    values = input(f'Введите значение переменных через запятую\n').split(',')
    for i, name in enumerate(parametrs.keys()):
        try:
            parametrs[name] = float(values[i].strip())
        except:
            print('Введите ЧИСЛА(разделитель точка)!!!')
            getParametrs()
    return parametrs


def findValuesX(parametrs):
    a, b, c, d = parametrs.values()
    p = getP(a, b, c)
    q = getQ(a, b, c, d)
    D = discriminant(p, q)
    A = (-1 * (q / 2) + D ** 0.5) ** (1 / 3)
    B = (-q / 2 - D ** 0.5) ** (1 / 3)
    y1 = A + B
    y2 = -1 * ((A + B) / 2) + 1j * ((A - B) / 2) * sqrt(3)
    y3 = -1 * ((A + B) / 2) - 1j * ((A - B) / 2) * sqrt(3)
    x1 = getX(y1, a, b)
    x2 = getX(y2, a, b)
    x3 = getX(y3, a, b)
    print(x1)
    print(checking(x1, **parametrs))
    print(x2)
    print(checking(x2, **parametrs))
    print(x3)
    print(checking(x3, **parametrs))
    return 0


def discriminant(p, q):
    return q ** 2 / 4 + p ** 3 / 27


def getP(a, b, c):
    return (3 * a * c - b ** 2) / (3 * a ** 2)


def getQ(a, b, c, d):
    return (2 * b ** 3 - 9 * a * b * c + 27 * a ** 2 * d) / (27 * a ** 3)


def getX(y, a, b):
    x = y - b / (3 * a)
    return x


def checking(x, **kwargs):
    a, b, c, d = kwargs.values()
    y = a * x ** 3 + b * x ** 2 + c * x + d
    if abs(y.real) <= 1 and abs(y.imag) <= 1:
        return f'{a} * {x} ^ 3 + {b} * {x} ^ 2 + {c} * {x} + {d} = {y} Допустимое отклонение\n'
    else:
        return f'{a} * {x} ^ 3 + {b} * {x} ^ 2 + {c} * {x} + {d} = {y} Недопустимое отклонение\n'


if __name__ == '__main__':
    parametrs = getParametrs()
    findValuesX(parametrs)