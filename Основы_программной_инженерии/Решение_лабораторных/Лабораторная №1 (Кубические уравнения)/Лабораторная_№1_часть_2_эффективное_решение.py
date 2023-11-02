from math import *
from numpy import *


def getParametrs():
    print('Эта программа считает корни уравнения по значениям a, b, c')
    print('Ссылка на алгоритм: https://ru.wikipedia.org/wiki/Тригонометрическая_формула_Виета')
    print('y = ax³ + bx² + cx + d')
    parametrs: dict = {'a': float, 'b': float, 'c': float, 'd': float}
    values = input(f'Введите значение переменных через запятую\n').split(',')
    for i, name in enumerate(parametrs.keys()):
        try:
            parametrs[name] = float(values[i].strip())
        except:
            print('Введите ЧИСЛА(разделитель точка)!!!')
            getParametrs()
    return parametrs


def findValuesX(parametrs):
    results = {}
    new_parametrs = divides_by_a(**parametrs)
    Q = getQ(**new_parametrs)
    R = getR(**new_parametrs)
    S = Q ** 3 - R ** 2

    if S > 0:
        f = (1 / 3) * arccos(R / sqrt(Q ** 3))
        y1 = - 2 * sqrt(Q) * cos(f)
        x1 = getX(y1, **new_parametrs)
        results['x1'] = x1

        y2 = - 2 * sqrt(Q) * cos(f + (2 / 3) * pi)
        x2 = getX(y2, **new_parametrs)
        results['x2'] = x2

        y3 = - 2 * sqrt(Q) * cos(f - (2 / 3) * pi)
        x3 = getX(y3, **new_parametrs)
        results['x3'] = x3

    elif S == 0:
        y1 = -2 * R ** (1 / 3)
        x1 = getX(y1, **new_parametrs)
        results['x1'] = x1

        y2 = R ** (1 / 3)
        x2 = getX(y2, **new_parametrs)
        results['x2'] = x2

    elif S < 0:
        if Q > 0:
            f = (1 / 3) * arccosh(abs(R) / sqrt(Q ** 3))

            y1 = - 2 * sign(R) * sqrt(Q) * cosh(f)
            x1 = getX(y1, **new_parametrs)
            results['x1'] = x1

            y2 = sign(R) * sqrt(Q) * cosh(f) + complex(0, sqrt(3) * sqrt(Q) * sinh(f))
            x2 = getX(y2, **new_parametrs)
            results['x2'] = x2

            y3 = sign(R) * sqrt(Q) * cosh(f) - complex(0, sqrt(3) * sqrt(Q) * sinh(f))
            x3 = getX(y3, **new_parametrs)
            results['x3'] = x3

        elif Q == 0:
            a, b, c = new_parametrs.values()
            y1 = - 1 * pow(c - (a / 3) ** 3, 1 / 3)
            x1 = getX(y1, **new_parametrs)
            results['x1'] = x1

            x2 = - 1 * (a + x1) / 2 + complex(0, 0.5 * sqrt(abs((a - 3 * x1) * (a + x1) - 4 * b)))
            results['x2'] = x2

            x3 = - 1 * (a + x1) / 2 - complex(0, 0.5 * sqrt(abs((a - 3 * x1) * (a + x1) - 4 * b)))
            results['x3'] = x3

        elif Q < 0:
            f = (1 / 3) * arcsinh(abs(R) / sqrt(abs(Q) ** 3))

            y1 = - 2 * sign(R) * sqrt(abs(Q)) * sinh(f)
            x1 = getX(y1, **new_parametrs)
            results['x1'] = x1

            y2 = sign(R) * sqrt(abs(Q)) * sinh(f) + complex(0, sqrt(3) * sqrt(abs(Q)) * cosh(f))
            x2 = getX(y2, **new_parametrs)
            results['x2'] = x2

            y3 = sign(R) * sqrt(abs(Q)) * sinh(f) - complex(0, sqrt(3) * sqrt(abs(Q)) * cosh(f))
            x3 = getX(y3, **new_parametrs)
            results['x3'] = x3

    answer = checking(**parametrs, **results)
    return answer


def divides_by_a(a, b, c, d):
    return {'a': b / a,
            'b': c / a,
            'c': d / a}


def discriminant(p, q):
    return q ** 2 / 4 + p ** 3 / 27


def getR(a, b, c):
    return (2 * a ** 3 - 9 * a * b + 27 * c) / 54


def getQ(a, b, c):
    return (a ** 2 - 3 * b) / 9


def getX(y, a, b, c):
    x = y - a / 3
    return x


def checking(a, b, c, d, **kwargs):
    answer = ''
    for name, value in kwargs.items():
        x = value
        answer += f'{name} = {value}\n'
        y = a * x ** 3 + b * x ** 2 + c * x + d
        if abs(y.real) <= 10 ** - 5 and abs(y.imag) <= 10 ** -5:
            answer += f'{a}*{name}³ + {b}*{name}² + {c}*{name} + {d} = {y} - Допустимое отклонение(<10^-5)\n\n'
        else:
            answer += f'{a}*{name}³ + {b}*{name}² + {c}*{name} + {d} = {y} - Недопустимое отклонение(>10^-5)\n\n'
    return answer


if __name__ == '__main__':
    parametrs = getParametrs()
    print(findValuesX(parametrs))