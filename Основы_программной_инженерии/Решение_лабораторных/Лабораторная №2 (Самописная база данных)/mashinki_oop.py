class Cars:
    def __init__(self, cars):
        self.cars = cars
        self.marka  = ''

baza = open("baza.txt.", encoding="utf-8").read()
with open('baza.txt') as f:
    lines = f.readlines()
count = len(lines)

command_list = ['Список доступных команд:'," - Добавить машину", " - Вывести список машин", ' - Изменить', ' - Удалить', ' - Поиск по характеристике']
for i in range(len(command_list)):
        print(command_list[i])

command = str(input())
head = ['Позиция','Марка', 'Модель', 'Цвет', 'Гос.номер', 'Находится на стоянке']
if command == 'Добавить машину':
    car = Cars('Car')
    f = open('baza.txt', 'a',encoding="utf-8" )
    count = str(count + 1)
    f.write(count)
    f.write(' ')
    print('Введите марку')
    car.marka = str(input())
    f.write(car.marka)
    f.write(' ')
    print('Введите модель')
    car.model = str(input())
    f.write(car.model)
    f.write(' ')
    print('Введите цвет машины')
    car.color = str(input())
    f.write(car.color)
    f.write(' ')
    print('Введите государственный номер')
    car.numb = str(input())
    f.write(car.numb)
    f.write(' ')
    print('Машина находится на стоянке?')
    car.place = str(input())
    f.write(car.place)
    f.write(' ')

    f.write("\n")
    f.close()
if command == 'Вывести список машин':
    print(baza)
if command == 'Изменить':
    with open('baza.txt',encoding="utf-8") as f:
        array = [row.strip() for row in f]
        for i in range(len(array)):
            a = (array[i]).split(' ')
            array[i] = a
    print('Введите позицию машины, харрактиристику которой хотите изменить')
    num = int(input())
    print('Какую харрактеристику вы хотели бы изменить?')
    characteristic = str(input())
    if characteristic == 'Марка':
        n_characteristic = 1
    if characteristic == 'Модель':
        n_characteristic = 2
    if characteristic == 'Цвет':
        n_characteristic = 3
    if characteristic == 'Гос.номер':
        n_characteristic = 4
    if characteristic == 'Находится на стоянке':
        n_characteristic = 5
    print('Введите новую характеристику')
    new_characteristic = str(input())
    for i in range(len(array)):
        if array[i][0] == str(num):
            array[i][n_characteristic] = new_characteristic
    array2 = []
    a = ''
    for i in range(len(array)):
        for j in range(len(array[i])):
            a += array[i][j] + ' '
        array2.append(a)
        a = ''
    f = open('baza.txt', 'w',encoding="utf-8" )
    for i in range(len(array2)):
        f.write(str(array2[i]))
        f.write('\n')
    f.close()
if command == 'Удалить':
    with open('baza.txt', encoding="utf-8") as f:
        array3 = [row.strip() for row in f]
        for i in range(len(array3)):
            a = (array3[i]).split(' ')
            array3[i] = a
    print('Введите позицию машины, которую хотите удалить')
    num2 = int(input())
    array4 = []
    a = ''
    for i in range(len(array3) - 1):
        if int(array3[i][0]) >= num2:
            array3[i][0] = str(int(array3[i][0]) - 1)
            array3[i] = array3[i + 1]
    for i in range(len(array3) - 1):
        for j in range(len(array3[i])):
            a += array3[i][j] + ' '
        array4.append(a)
        a = ''
    f = open('baza.txt', 'w', encoding="utf-8")
    for i in range(len(array4)):
        f.write(str(array4[i]))
        f.write('\n')
    f.close()
if command == "Поиск по характеристике":
    print('Введите название характеристики, по которой хотите найти машину')
    characteristic = str(input())
    print('Введите саму характеристику')
    target_characteristic = str(input())
    n_characteristic = 0
    if characteristic == 'Марка':
         n_characteristic = 1
    if characteristic == 'Модель':
         n_characteristic = 2
    if characteristic == 'Цвет':
        n_characteristic = 3
    if characteristic == 'Гос.номер':
        n_characteristic = 4
    if characteristic == 'Находится на стоянке':
        n_characteristic = 5
    with open('baza.txt',encoding="utf-8") as f:
        array = [row.strip() for row in f]
        for i in range(len(array)):
            a = (array[i]).split(' ')
            array[i] = a
    array2=[]
    for i in range(len(array)):
        if array[i][n_characteristic] == target_characteristic:
           array2.append(array[i])

    for i in range(len(array2)):
        c = ''
        for j in range(len(array2[i])):
            c += array2[i][j] + ' '
        print(c)