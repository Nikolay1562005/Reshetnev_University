import json


data = {}
table = 0


def open_json_db(sours_on_file):
    with open(sours_on_file, 'r') as file:
        return json.load(file)


def open_table(name_table):
    if name_table in data[1].keys():
        return data[name_table]
    else:
        print("Такой таблицы нет :(")
        all_tables()
        return -1


def add_table(name_table):
    if name_table not in data.keys():
        data[name_table] = {}
        return data[name_table]
    else:
        print("Такая таблица уже есть")
        return -1


def delete_table(name_table):
    if name_table in data.keys():
        del data[name_table]
        print(f"Успешно удалена таблица {name_table}")
    else:
        print("Такой таблицы нет")
        all_tables()
        return -1


def all_tables():
    return data[1].keys()


def to_json_db(sours_on_file):
    with open(sours_on_file, 'w') as file:
        json.dump(data, file, indent=4)


def add_field(name_field, type_filed, value_field):
    if type_filed == "число":
        table[name_field] = int(value_field)
    if type_filed == "строка":
        table[name_field] = value_field
    if type_filed == "список":
        table[name_field] = value_field.split(' ')


def delit_field(name_field):
    if name_field in table.keys():
        del table[name_field]
        print(f"Успешно удалено поле {name_field}")
    else:
        print("Такого поля нет")
        all_fields()
        return -1


def change_field(name_field, type_filed, value_field):
    if name_field in table.keys():
        if type_filed == "число":
            table[name_field] = int(value_field)
        if type_filed == "строка":
            table[name_field] = value_field
        if type_filed == "список":
            table[name_field] = value_field.split(' ')
    else:
        print("Такого поля нет")
        all_fields()
        return -1


def all_fields():
    return table


def save_changes(name_table, sours_on_file):
    data[name_table] = table
    to_json_db(sours_on_file)


if __name__ == '__main__':
    sours_on_file = "MyDB.json"
    data = open_json_db(sours_on_file)
    choice_name_table = ''

    while True:
        command = input(f"{choice_name_table}> ")
        command_in_lowercase = command.lower().strip()
        command_splited = command.strip().split(' ')
        try:
            if choice_name_table == '':
                if "открыть таблицу" in command_in_lowercase:
                    table = open_table(' '.join(command_splited[2:]))
                    if table != -1:
                        choice_name_table = ' '.join(command_splited[2:])

                elif "имена таблиц" in command_in_lowercase:
                    for name_table in all_tables():
                        print(name_table)

                elif "создать таблицу" in command_in_lowercase:
                    table = add_table(' '.join(command_splited[2:]))
                    if table != -1:
                        choice_name_table = ' '.join(command_splited[2:])

                elif "удалить таблицу" in command_in_lowercase:
                    delete_table(' '.join(command_splited[2:]))

                elif "поле" in command_in_lowercase:
                    print("Откройте таблицу!!!")

            elif choice_name_table != '':

                if "имена полей" in command_in_lowercase:
                    for field, value in all_fields().items():
                        print(f"{field} : {value}")

                elif "добавить поле" in command_in_lowercase:
                    add_field(command_splited[2], command_splited[3], ' '.join(command_splited[4:]))

                elif "удалить поле" in command_in_lowercase:
                    delit_field(command_splited[2])

                elif "изменить поле" in command_in_lowercase:
                    change_field(command_splited[2], command_splited[3], ' '.join(command_splited[4:]))

                elif "сохранить таблицу" in command_in_lowercase:
                    save_changes(choice_name_table, sours_on_file)
                    choice_name_table = ''
                    print("Успешно сохранено ;)")

                elif "таблиц" in command_in_lowercase:
                    print("Сначало сохраните таблицу!!!")

            else:
                print("неверная команда!")

            if "помощь" in command_in_lowercase:
                print(
                    '''
Комманды:
открыть таблицу <название таблицы> - переносит в поле выбранной таблицы
имена таблиц - выводит список имеющихся таблиц
создать таблицу <название таблицы> - создаёт новую пустую таблицу
удалить таблицу <название таблицы> - удаляет таблицу по полному названию
закрыть программу - прерыват работу программы
имена полей - выводит имена полей при наличии открытой таблицы
добавить поле <название поля> <тип поля> <значение(ия)> - добавляет именнованое поле
одного из типов: число, строка, список
удалить поле <название поля> - удаляет поле по полному названию
изменить поле <название поля> <тип поля> <значение(ия)> - работает как добавить поле, но проверяет наличее поля
сохранить таблицу <название таблицы> - потгружает изменённые/созданные данные в файл
                    '''
                )
            elif "закрыть программу" in command_in_lowercase:
                break

        except:
            print("ошибка в команде!")