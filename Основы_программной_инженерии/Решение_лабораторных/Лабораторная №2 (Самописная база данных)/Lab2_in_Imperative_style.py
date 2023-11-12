import json

data = {}
table = 0
sours_on_file = "MyDB.json"
with open(sours_on_file, 'r') as file:
    data = json.load(file)

choice_name_table = ''

while True:
    command = input(f"{choice_name_table}> ")
    list_simbol = list(command)
    command_in_lowercase = ''
    #-----------------
    # lower()
    for i in list_simbol:
        utf = ord(i)
        if 1040 <= utf <1072:
            command_in_lowercase += chr(utf + 32)
        else:
            command_in_lowercase += i
    #-----------------

    # split()
    command_splited = []
    word = ''
    for char in command + ' ':
        if ' ' == char:
            command_splited += [word]
            word = ''
        else:
            word += char
    try:
        if choice_name_table == '':
            if "открыть таблицу" in command_in_lowercase:
                print(command_splited)
                name_table = command_splited[2]
                if name_table in data[1]:
                    table = data[1][name_table]
                    choice_name_table = name_table
                else:
                    print("Такой таблицы нет :(")
                    for name_table in data[1]:
                        print(name_table)

            elif "найти машину по" in command_in_lowercase:
                #----------------------------------
                # split()
                parametrs = []
                word = ''
                for char in command_splited[3:] + ' ':
                    if ' ' == char:
                        parametrs += [word]
                        word = ''
                    else:
                        word += char
                #----------------------------------
                        
                list_fauded_cars = {}
                for table in data[1]:
                    if all([parametr in str(tables[table]).lower() for parametr in parametrs]):
                        list_fauded_cars[table] = tables[table]
                    
                for care in list_fauded_cars:
                    if care in self.carpark.values():
                        print(f"На стоянке есть подходящая машина {care}")
                        
                for care in list_fauded_cars:
                    table = list_fauded_cars[care]
                    print(f"{care} : ")
                    for field in table:
                        print(f"\t{field} : {table[field]}")

            elif "стоянка" in command_in_lowercase:
                for name_table in data[0]:
                    name_care = data[0][name_table]
                    if name_care != None:
                        print(f"Место №{name_table} занто {name_care}")
                    else:
                        print(f"Место №{name_table} свободно")

            elif "освободиь место" in command_in_lowercase:
                if command_splited[2] in data[0]:
                    data[0][command_splited[2]] = None
                else:
                    print(f"Место №{command_splited[2]} и так свободно")
                    
            elif "занять место" in command_in_lowercase:
                if command_splited[2] in data[0] and int(command_splited[2]) <= 100:
                    if data[0][command_splited[2]] == None:
                        data[0][command_splited[2]] = command_splited[3]
                    else:
                        print(f"Место №{number_plase} занто {self.carpark[number_plase]}")
               
            elif "имена таблиц" in command_in_lowercase:
                for name_table in data[1]:
                    print(name_table)

            elif "создать таблицу" in command_in_lowercase:
                name_table = command_splited[2]
                if name_table not in data[1]:
                    data[name_table][1] = {}
                    table = data[1][name_table]
                    choice_name_table = name_table
                else:
                    print("Такая таблица уже есть")
                    for name_table in data[1]:
                        print(name_table)


            elif "удалить таблицу" in command_in_lowercase:
                name_table = command_splited[2]
                if name_table in data[1]:
                    del data[1][name_table]
                    print(f"Успешно удалена таблица {name_table}")
                else:
                    print("Такой таблицы нет")
                    for name_table in data[1]:
                        print(name_table)

            elif "поле" in command_in_lowercase:
                print("Откройте таблицу!!!")

        elif choice_name_table != '':

            if "имена полей" in command_in_lowercase:
                for i in table:
                    field, value = i, table[i]
                    print(f"{field} : {value}")

            elif "добавить поле" in command_in_lowercase:
                name_field = command_splited[2]
                type_filed = command_splited[3]
                value_field = ''
                # " ".join()
                for value in command_splited[4:]:
                    value_field += value
                    value_field += " "
                value_field -= " "
                
                if type_filed == "число":
                    table[name_field] = int(value_field)
                if type_filed == "строка":
                    table[name_field] = value_field
                if type_filed == "список":
                    value_splited = []
                    value = ""
                    for char in value_field + ' ':
                        if ' ' == char:
                            command_splited += [word]
                            value = ''
                        else:
                            word += char
                        table[name_field] = value_splited
            elif "удалить поле" in command_in_lowercase:
                name_field = command_splited[2]
                if name_field in table:
                    del table[name_field]
                    print(f"Успешно удалено поле {name_field}")
                else:
                    for i in table:
                        field, value = i, table[i]
                        print(f"{field} : {value}")

            elif "изменить поле" in command_in_lowercase:
                name_field = command_splited[2]
                type_filed = command_splited[3]
                value_field = ''
                # " ".join()
                for value in command_splited[4:]:
                    value_field += value
                    value_field += " "
                value_field -= " "
                if name_field in table:
                    if type_filed == "число":
                        table[name_field] = int(value_field)
                    if type_filed == "строка":
                        table[name_field] = value_field
                    if type_filed == "список":
                        value_splited = []
                        value = ""
                        for char in value_field + ' ':
                            if ' ' == char:
                                command_splited += [word]
                                value = ''
                            else:
                                word += char
                        table[name_field] = value_splited
                else:
                    print("Такого поля нет")
                    for i in table:
                        field, value = i, table[i]
                        print(f"{field} : {value}")

            elif "сохранить таблицу" in command_in_lowercase:
                data[1][name_table] = table
                with open(sours_on_file, 'w') as file:
                    json.dump(data, file, indent=4)
                    print("Успешно сохранено ;)")
                choice_name_table = ""

            elif "таблиц" in command_in_lowercase:
                print("Сначало сохраните таблицу!!!")

        else:
            print("неверная команда!")

        if "помощь" in command_in_lowercase:
            print(
'''
Комманды:
найти машину по <люые данные которые могут быть у машины через пробел> - выводит список всех машин удовлетворяющих условию
стоянка - выводит список всех мест на стоянке и занимаемых ими местах
освободиь место <номер места> - освобождает место по требованию
занять место <номер места> <номер машины> - занимает место если оно свободно
открыть таблицу <номер машины> - переносит в поле выбранной таблицы
имена таблиц - выводит список имеющихся таблиц
создать таблицу <номер машины> - создаёт новую пустую таблицу
удалить таблицу <номер машины> - удаляет таблицу по полному названию
закрыть программу - прерыват работу программы
имена полей - выводит имена полей при наличии открытой таблицы
добавить поле <название поля> <тип поля> <значение(ия)> - добавляет именнованое поле одного из типов: число, строка, список
удалить поле <название поля> - удаляет поле по полному названию
изменить поле <название поля> <тип поля> <значение(ия)> - работает как добавить поле, но проверяет наличее поля
сохранить таблицу <название таблицы> - потгружает изменённые/созданные данные в файл в основном нужна, чтоб выйти из таблицы
'''
            )
        elif "закрыть программу" in command_in_lowercase:
            break

    except:
        print("ошибка в команде!")