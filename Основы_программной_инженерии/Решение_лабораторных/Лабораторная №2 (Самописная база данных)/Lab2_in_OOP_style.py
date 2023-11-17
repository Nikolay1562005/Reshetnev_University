import json
from texttable import Texttable


class JsonDB:
    def __init__(self, sours_on_file):
        self.sours_on_file = sours_on_file
        with open(self.sours_on_file, 'r') as file:
            data = json.load(file)

        self._create_attributes(data)

    def _create_attributes(self, data):
        for name, value in data[1].items():
            setattr(self, name, value)
        setattr(self, "carpark", data[0])

    # -----------------------------------------------

    def open_table(self, name_table):
        if name_table in self.all_tables():
            return ObjectsDB(name_table, getattr(self, name_table), self)
        return -1

    # ---------------------------------------------

    def all_parking_plases(self):
        return self.carpark


    def free_up_parking_plase(self, number_plase):
        if number_plase in self.all_parking_plases():
            self.carpark[number_plase] = None
            self._to_json()
            return self.all_parking_plases()
        else:
            return -1

    def add_car_to_carepark(self, number_plase, name_care):
        if name_care == None or int(number_plase) < 1 or int(number_plase) > len(self.carpark):
            return -1
        elif number_plase in self.carpark:
            if self.carpark[number_plase] == None:
                self.carpark[number_plase] = name_care
                self._to_json()
                if name_care not in self.all_tables():
                    self.add_table(name_care)
                    return self.open_table(name_care)
                return self.all_parking_plases()
            else:
                return {number_plase: self.carpark[number_plase]}

    # -----------------------------------------------------------------------------

    def add_table(self, name_table):
        if name_table not in self.all_tables():
            setattr(self, name_table, {})
            self._to_json()
            return ObjectsDB(name_table, getattr(self, name_table), self)
        else:
            return -1

    def delete_table(self, name_table):
        if name_table in self.all_tables():
            delattr(self, name_table)
            self._to_json()
            return self.all_tables()
        else:
            return -1

    def all_tables(self):
        tables = vars(self).copy()
        del tables["sours_on_file"]
        del tables["carpark"]
        return tables

    def find_care(self, parametrs):
        list_fauded_cars = {}
        tables = self.all_tables()
        for table in tables:
            if all([parametr in str(tables[table]).lower() for parametr in parametrs]):
                list_fauded_cars[table] = tables[table]

        for care in list_fauded_cars:
            if care in self.carpark.values():
                list_fauded_cars[care]["есть на стоянке"] = "Да"
            else:
                list_fauded_cars[care]["есть на стоянке"] = "Нет"

        return list_fauded_cars

    def _update_table(self, name_table, data_from_table):
        setattr(self, name_table, data_from_table)
        self._to_json()

    def _to_json(self):
        with open(self.sours_on_file, 'w') as file:
            json.dump([self.all_parking_plases(), self.all_tables()], file, indent=4)


class ObjectsDB:
    def __init__(self, name_table, data, parent_class):
        self.parent_class = parent_class
        self.name_table = name_table
        for name, value in data.items():
            setattr(self, name, value)

    def __str__(self):
        return self.name_table

    def all_fields(self):
        fields = vars(self).copy()
        del fields['name_table']
        del fields['parent_class']
        return fields

    def add_field(self, name_field, type_filed, value_field):
        if name_field not in self.all_fields():
            try:
                if type_filed == "int":
                    setattr(self, name_field, int(value_field))
                elif type_filed == "str":
                    setattr(self, name_field, value_field)
                elif type_filed == "list":
                    setattr(self, name_field, value_field.split(' '))
            except:
                return -1
            self.save_changes()
            return self.all_fields()
        else:
            return -1

    def delit_field(self, name_field):
        if name_field in self.all_fields():
            delattr(self, name_field)
            self.save_changes()
            return self.all_fields()
        else:
            return -1

    def change_field(self, name_field, type_filed, value_field):
        if name_field in self.all_fields():
            try:
                if type_filed == "int":
                    setattr(self, name_field, int(value_field))
                elif type_filed == "str":
                    setattr(self, name_field, value_field)
                elif type_filed == "list":
                    setattr(self, name_field, value_field.split(' '))
            except:
                return -1
            self.save_changes()
            return self.all_fields()
        else:
            return -1

    def save_changes(self):
        self.parent_class._update_table(self.name_table, self.all_fields())


def crete_console_table(title, data):
    data = {"Номер машины": title} | data
    for name_field in data:
        if isinstance(data[name_field], list):
            data[name_field] = ", ".join(data[name_field])

    t = Texttable()
    t.add_rows([[name_field for name_field in data],
               [str(value) for value in data.values()]])
    print(t.draw())



if __name__ == '__main__':
    db = JsonDB("MyDB.json")
    choice_table = ''
    while True:
        command = input(f"{str(choice_table)}> ")
        command_in_lowercase = command.lower().strip()
        command_splited = command.strip().split(' ')
        try:
            if choice_table == '':
                if "открыть таблицу" in command_in_lowercase:
                    name_table = ' '.join(command_splited[2:])
                    table = db.open_table(name_table)
                    if table != -1:
                        name_care = str(table)
                        fields = table.all_fields()
                        crete_console_table(name_care, fields)
                        choice_table = table
                    else:
                        print("Такой таблицы нет :(")

                elif "имена таблиц" in command_in_lowercase:
                    tables = db.all_tables()
                    for care, table in tables.items():
                        crete_console_table(care, table)

                elif "найти машину по" in command_in_lowercase:
                    search_parameters = command_splited[3:]
                    list_cars = db.find_care(search_parameters).items()
                    for care, table in list_cars:
                        crete_console_table(care, table)

                elif "создать таблицу" in command_in_lowercase:
                    choice_table = db.add_table(command_splited[2])

                elif "удалить таблицу" in command_in_lowercase:
                    db.delete_table(command_splited[2:])

                elif "изменить количество мест на" in command_in_lowercase:
                    carpark = db.change_count_plases_in_carepark(command_splited[4])
                    if carpark == -1:
                        print("Вы ввели не корректное количество мест")
                    else:
                        t = Texttable()
                        t.add_rows([["место", "машина", "место", "машина", "место", "машина", "место", "машина"]] +
                                   [[str(i + 1), carpark[str(i + 1)],
                                     str(i + 26), carpark[str(i + 26)],
                                     str(i + 51), carpark[str(i + 51)],
                                     str(i + 76), carpark[str(i + 76)],
                                     ] for i in range(25)])
                        print(t.draw())

                elif "стоянка" in command_in_lowercase:
                    carpark = db.all_parking_plases()
                    t = Texttable()
                    t.add_rows([["место", "машина", "место", "машина", "место", "машина", "место", "машина"]] +
                               [[str(i + 1), carpark[str(i + 1)],
                                 str(i + 26), carpark[str(i + 26)],
                                 str(i + 51), carpark[str(i + 51)],
                                 str(i + 76), carpark[str(i + 76)],
                                 ] for i in range(25)])
                    print(t.draw())

                elif "освободиь место" in command_in_lowercase:
                    plase = db.free_up_parking_plase(command_splited[2])
                    if plase == -1:
                        print(f"Такого места №{command_splited[2]} - нет")


                elif "занять место" in command_in_lowercase:
                    plase = db.add_car_to_carepark(command_splited[2], command_splited[3])
                    if isinstance(plase, ObjectsDB):
                        print(f"Информации по машине {command_splited[3]} - нет")
                        print("Заполните данные о машине:")
                        choice_table = plase

                    elif plase[command_splited[2]] != command_splited[3]:
                        print(f"Место №{command_splited[2]} занто {plase[command_splited[2]]}")

                elif "изменить место на" in command_in_lowercase:
                    choice_table.change_place(int(command_splited[3]))
                    carpark = db.all_parking_plases()
                    t = Texttable()
                    t.add_rows([["место", "машина", "место", "машина", "место", "машина", "место", "машина"]] +
                               [[str(i + 1), carpark[str(i + 1)],
                                 str(i + 26), carpark[str(i + 26)],
                                 str(i + 51), carpark[str(i + 51)],
                                 str(i + 76), carpark[str(i + 76)],
                                 ] for i in range(25)])
                    print(t.draw())

                elif "поле" in command_in_lowercase:
                    print("Откройте таблицу!!!")


            elif choice_table != '':

                if "имена полей" in command_in_lowercase:
                    crete_console_table(str(choice_table), choice_table.all_fields())

                elif "добавить поле" in command_in_lowercase:
                    choice_table.add_field(command_splited[2], command_splited[3], ' '.join(command_splited[4:]))
                    crete_console_table(str(choice_table), choice_table.all_fields())

                elif "удалить поле" in command_in_lowercase:
                    choice_table.delit_field(command_splited[2])
                    crete_console_table(str(choice_table), choice_table.all_fields())

                elif "изменить поле" in command_in_lowercase:
                    choice_table.change_field(command_splited[2], command_splited[3], ' '.join(command_splited[4:]))
                    crete_console_table(str(choice_table), choice_table.all_fields())

                elif "закрыть таблицу" in command_in_lowercase:
                    choice_table = ''

                elif "таблиц" in command_in_lowercase:
                    print("Сначало сохраните таблицу!!!")

            else:
                print("неверная команда!")

            if "помощь" in command_in_lowercase:
                print(
'''Комманды:
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
закрыть таблицу - в основном нужна, чтоб выйти из таблицы''')
            elif "закрыть программу" in command_in_lowercase:
                break

        except:
            print("ошибка в команде!")