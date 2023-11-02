def getParametrs():
    print('Эта программа считает корни уравнения по значениям a, b, c')
    print('y = a * x ^ 2 + b * x + c')
    parametrs = {'a': 0, 'b': 0, 'c': 0}
    values = input(f'Введите значение переменных через запятую\n').split(',')
    for i, name in enumerate(parametrs.keys()):
        try:
            parametrs[name] = float(values[i].strip())
        except:
            print('Введите ЧИСЛА!!!')
            getParametrs()
    return parametrs

def discriminant(a, b, c):
    return (b**2) - 4 * a * c

def checking(x, a, b, c):
    y = a * (x ** 2) + b * x + c
    if abs(y) <= 1:
        return f'{a} * {x} ^ 2 + {b} * {x} + {c} = {y} Допустимое отклонение\n'
    else:
        return f'{a} * {x} ^ 2 + {b} * {x} + {c} = {y} Недопустимое отклонение\n'
def findValuesX(parametrs):
    a, b, c = parametrs.values()

    D = discriminant(a, b, c)
    print(f'D = {D}')
    result = ''
    if D == 0:
        x = (-b) / (2 * a)
        result += f'X = {x}\n'
        result += checking(x, a, b, c)
    elif D > 0:
        x1 = (-b + (D**0.5)) / (2 * a)
        result += f'X1 = {x1}\n'
        result += checking(x1, a, b, c)

        x2 = (-b - (D**0.5)) / (2 * a)
        result += f'X2 = {x2}\n'
        result += checking(x2, a, b, c)
    else:
        result += 'Данное квадратное уравнение корней не имеет\n'
    return result

if __name__ == '__main__':
    parametrs = getParametrs()
    print(findValuesX(parametrs))