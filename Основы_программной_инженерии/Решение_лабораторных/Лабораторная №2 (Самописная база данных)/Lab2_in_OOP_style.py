import json
from texttable import Texttable

t = Texttable()


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
        if name_table in vars(self) and name_table != "carpark":
            return ObjectsDB(name_table, getattr(self, name_table))
        print("Такой таблицы нет :(")
        self.all_tables()
        return -1

    # ---------------------------------------------

    def all_parking_plases(self):
        t.add_rows([["место", "машина", "место", "машина", "место", "машина", "место", "машина"]] +
                   [[str(i + 1), self.carpark[str(i + 1)],
                     str(i + 26), self.carpark[str(i + 26)],
                     str(i + 51), self.carpark[str(i + 51)],
                     str(i + 76), self.carpark[str(i + 76)],
                     ] for i in range(25)])
        print(t.draw())
        return self.carpark

        # for number_plase, name_care in self.carpark.items():
        #     if name_care != None:
        #         print(f"Место №{number_plase} занто {name_care}")
        #     else:
        #         print(f"Место №{number_plase} свободно")

    def free_up_parking_plase(self, number_plase):
        if number_plase in self.carpark:
            self.carpark[number_plase] = None
            self._to_json()
        else:
            print(f"Место №{number_plase} и так свободно")

    def add_car_to_carepark(self, number_plase, name_care):
        if number_plase in self.carpark and int(number_plase) <= 100:
            if self.carpark[number_plase] == None:
                self.carpark[number_plase] = name_care
                self._to_json()
            else:
                print(f"Место №{number_plase} занто {self.carpark[number_plase]}")

    # -----------------------------------------------------------------------------

    def add_table(self, name_table):
        if name_table not in vars(self):
            self._to_json()
            return ObjectsDB(name_table, getattr(self, name_table))
        else:
            print("Такая таблица уже есть")

    def delete_table(self, name_table):
        tables = vars(self).copy()
        del tables["sours_on_file"]
        del tables["carpark"]
        if name_table in tables:
            delattr(self, name_table)
            self._to_json()
            return f"Успешно удалена таблица {name_table}"
        else:
            print("Такой таблицы нет")
            self.all_tables()
            return -1

    def all_tables(self):
        tables = vars(self).copy()
        del tables["sours_on_file"]
        return tables.keys()

    def find_care(self, parametrs):
        list_fauded_cars = {}
        tables = vars(self).copy()
        del tables["sours_on_file"]
        del tables["carpark"]
        for table in tables:

            if all([parametr in str(tables[table]).lower() for parametr in parametrs]):
                list_fauded_cars[table] = tables[table]

        for care in list_fauded_cars:
            if care in self.carpark.values():
                print(f"На стоянке есть подходящая машина {care}")
        return list_fauded_cars

    def _update_table(self, name_table, data_from_table):
        setattr(self, name_table, data_from_table)
        self._to_json()

    def _to_json(self):

        with open(self.sours_on_file, 'w') as file:
            tables = vars(self).copy()
            del tables["sours_on_file"]
            del tables["carpark"]
            json.dump([self.carpark, tables], file, indent=4)


class ObjectsDB:
    def __init__(self, name_table, data):

        for name, value in data.items():
            setattr(self, name, value)
        self.name_table = name_table

    def __str__(self):
        return self.name_table

    def all_fields(self):
        fields = vars(self).copy()
        del fields['name_table']
        return fields

    def add_field(self, name_field, type_filed, value_field):
        if type_filed == "число":
            setattr(self, name_field, int(value_field))
        if type_filed == "строка":
            setattr(self, name_field, value_field)
        if type_filed == "список":
            setattr(self, name_field, value_field.split(' '))

    def delit_field(self, name_field):
        if delattr(self, name_field) == 0:
            print(f"поле {name_field}успешно удалено")
        else:
            print("Такого поля нет")
            self.all_fields()
            return -1

    def change_field(self, name_field, type_filed, value_field):
        if name_field in vars(self):
            if type_filed == "число":
                setattr(self, name_field, int(value_field))
            if type_filed == "строка":
                setattr(self, name_field, value_field)
            if type_filed == "список":
                setattr(self, name_field, value_field.split(' '))
        else:
            print("Такого поля нет")
            self.all_fields()
            return -1

    def save_changes(self, collection_class):
        fields = vars(self).copy()
        del fields['name_table']
        collection_class._update_table(self.name_table, fields)


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
                    table = db.open_table(' '.join(command_splited[2:]))
                    if table != -1:
                        choice_table = table

                elif "найти машину по" in command_in_lowercase:
                    list_cars = db.find_care(command_splited[3:]).items()
                    for care, table in list_cars:
                        print(f"{care} : ")
                        for field, value in table.items():
                            print(f"\t{field} : {value}")

                elif "стоянка" in command_in_lowercase:
                    db.all_parking_plases()

                elif "освободиь место" in command_in_lowercase:
                    db.free_up_parking_plase(command_splited[2])

                elif "занять место" in command_in_lowercase:
                    db.add_car_to_carepark(command_splited[2], command_splited[3])

                elif "имена таблиц" in command_in_lowercase:
                    for name_table in db.all_tables():
                        print(name_table)

                elif "создать таблицу" in command_in_lowercase:
                    choice_table = db.add_table(' '.join(command_splited[2:]))

                elif "удалить таблицу" in command_in_lowercase:
                    db.delete_table(' '.join(command_splited[2:]))

                elif "поле" in command_in_lowercase:
                    print("Откройте таблицу!!!")


            elif choice_table != '':

                if "имена полей" in command_in_lowercase:
                    for field, value in choice_table.all_fields().items():
                        print(f"{field} : {value}")

                elif "добавить поле" in command_in_lowercase:
                    choice_table.add_field(command_splited[2], command_splited[3], ' '.join(command_splited[4:]))
                    choice_table.save_changes(db)

                elif "удалить поле" in command_in_lowercase:
                    choice_table.delit_field(command_splited[2])
                    choice_table.save_changes(db)

                elif "изменить поле" in command_in_lowercase:
                    choice_table.change_field(command_splited[2], command_splited[3], ' '.join(command_splited[4:]))
                    choice_table.save_changes(db)

                elif "изменить место на" in command_in_lowercase:
                    choice_table.change_place(int(command_splited[3]))
                    choice_table.save_changes(db)

                elif "убрать машину" in command_in_lowercase:
                    choice_table.delit_place()
                    choice_table.save_changes(db)

                elif "сохранить таблицу" in command_in_lowercase:
                    choice_table = ''
                    print("Успешно сохранено ;)")

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
сохранить таблицу <название таблицы> - потгружает изменённые/созданные данные в файл в основном нужна, чтоб выйти из таблицы''')
            elif "закрыть программу" in command_in_lowercase:
                break

        except:
            print("ошибка в команде!")