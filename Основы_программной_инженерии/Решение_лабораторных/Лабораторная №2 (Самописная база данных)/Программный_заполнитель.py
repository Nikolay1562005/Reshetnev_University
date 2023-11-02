from random import choice, randrange, randint

from Lab2_in_OOP_style import JsonDB

names = [
    "Audi A4",
    "BMW 3 Series",
    "Mercedes - Benz C - Class",
    "Volkswagen Golf",
    "Ford Mustang",
    "Chevrolet Camaro",
    "Toyota Camry",
    "Honda Civic",
    "Nissan Altima",
    "Subaru Impreza",
    "Tesla Model S",
    "Porsche 911",
    "Lamborghini Aventador",
    "Ferrari 488 GTB",
    "Aston Martin DB11",
    "Jaguar F - Type",
    "Land Rover Range Rover",
    "Jeep Wrangler",
    "GMC Sierra",
    "Cadillac Escalade",
]
colors = [
    "Красный",
    "Оранжевый",
    "Желтый",
    "Зеленый",
    "Голубой",
    "Синий",
    "Фиолетовый",
    "Розовый",
    "Белый",
    "Черный",
    "Серый",
    "Коричневый",
    "Бежевый",
    "Оливковый",
    "Малиновый",
    "Лимонный",
    "Бирюзовый",
    "Лиловый",
    "Серебряный",
    "Золотой",
]

regions = ['A', 'B', 'C', 'E', 'H', 'K', 'M', 'O', 'P', 'T', 'X', 'Y']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
def generate_number():
    number = ''
    number += choice(regions) + choice(regions)
    number += str(randint(10, 21))
    number += choice(numbers) + choice(numbers) + choice(numbers)
    return number


db = JsonDB("MyDB.json")

tables = db.all_tables()
# функции для управления таблицами
# db.add_table("имя таблицы")
# db.delete_table("имя таблицы")
# db.find_care("любой набор данных о искомой машине через пробелл")

carepark = db.all_parking_plases()
# функционал стоянки
# db.free_up_parking_plase("номер места для освобождения")
# db.add_car_to_carepark("номер места", "номер машины")

for table in tables:
    choice_table = db.open_table(table)
    fields = choice_table.all_fields()
    # функционал таблицы
    # choice_table.add_field("имя поля", "тип поля", "значения")
    # choice_table.delit_field("имя поля")
    # choice_table.change_field("имя поля", "тип поля", "значения")
    # choice_table.save_changes(db)