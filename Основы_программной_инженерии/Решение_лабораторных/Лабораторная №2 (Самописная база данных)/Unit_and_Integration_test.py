import unittest
import json

from Lab2_in_OOP_style import JsonDB, ObjectsDB


class UnitTestJsonDB(unittest.TestCase):
    def setUp(self):
        self.test_care = "TestCareKH14472"
        self.sours_on_file ='MyDB.json'
        self.db = JsonDB(self.sours_on_file)
        with open(self.sours_on_file, 'r') as file:
            self.data = json.load(file)

    def tearDown(self):
        self.db.delete_table(self.test_care)


    def update_data_from_db(self):
        with open(self.sours_on_file, 'r') as file:
            self.data = json.load(file)


    def test_open_table(self):
        self.assertEqual(self.db.open_table(self.test_care), -1)
        self.assertEqual(self.db.open_table("carpark"), -1)
        self.db.add_table(self.test_care)
        self.assertEqual(str(self.db.open_table(self.test_care)), self.test_care)
        self.db.delete_table(self.test_care)

    def test_on_current_information(self):
        self.update_data_from_db()
        carepark = self.data[0]
        self.assertDictEqual(self.db.all_parking_plases(), carepark)
        tables = self.data[1]
        self.assertDictEqual(self.db.all_tables(), tables)


    def test_free_up_parking_plase(self):
        count_plases = len(self.db.carpark)
        old_care = self.db.carpark[str(count_plases - 1)]
        self.assertDictEqual(self.db.free_up_parking_plase(str(count_plases - 1)),
                             self.db.all_parking_plases())
        self.assertEqual(self.db.free_up_parking_plase(str(-5)), -1)
        self.assertEqual(self.db.free_up_parking_plase(str(count_plases + 1)), -1)

        self.db.carpark[str(count_plases - 1)] = old_care

    def test_add_car_to_carepark(self):
        count_plases = len(self.db.carpark)

        self.assertEqual(self.db.add_car_to_carepark(str(count_plases - 1), None), -1)

        self.assertEqual(self.db.add_car_to_carepark(str(count_plases + 1), self.test_care), -1)
        self.assertEqual(self.db.add_car_to_carepark(str(-5), self.test_care), -1)
        self.assertEqual(self.db.add_car_to_carepark(str(0), self.test_care), -1)

        old_care = self.db.carpark[str(count_plases)]
        self.db.delete_table(self.test_care)
        self.assertEqual(str(self.db.add_car_to_carepark(str(count_plases), self.test_care)), self.test_care)
        self.assertEqual(self.db.add_car_to_carepark(str(count_plases), self.test_care),
                         {str(count_plases): self.test_care})

        self.db.carpark[str(count_plases)] = old_care
        self.db.delete_table(self.test_care)

    def test_add_table(self):
        self.assertEqual(str(self.db.add_table(self.test_care)), self.test_care)
        self.assertEqual(self.db.add_table(self.test_care), -1)

        self.db.delete_table(self.test_care)

    def test_delete_table(self):
        self.assertEqual(self.db.delete_table(self.test_care), -1)

        self.db.add_table(self.test_care)
        self.assertEqual(self.db.delete_table(self.test_care), self.db.all_tables())

    def test_find_care(self):
        parametrs = ["красный"]
        care = self.db.find_care(parametrs)
        self.assertEqual(all([parametr in str(care).lower() for parametr in parametrs]), True)


class UnitTestObjectsDB(unittest.TestCase):
    def setUp(self):
        self.sours_on_file ='MyDB.json'
        self.db = JsonDB(self.sours_on_file)
        self.test_care = "TestCareKH14472"
        self.table = self.db.add_table(self.test_care)
        with open(self.sours_on_file, 'r') as file:
            self.data = json.load(file)

    def tearDown(self):
        self.db.delete_table(self.test_care)


    def test_all_fields(self):
        self.assertDictEqual(self.table.all_fields(),
                             self.data[1][self.test_care])

    def test_add_field(self):
        self.assertDictEqual(self.table.add_field("цена", "int", "1000000"),
                             self.db.all_tables()[self.test_care])
        self.assertEqual(self.table.add_field("цена", "int", "милион"), -1)
        self.assertDictEqual(self.table.add_field("цвет", "str", "Зелёный"),
                             self.db.all_tables()[self.test_care])
        self.assertEqual(self.table.add_field("цвет", "str", "Зелёный"), -1)
        self.assertDictEqual(self.table.add_field("компоненты", "list", "Зелёный колёса фары 67"),
                             self.db.all_tables()[self.test_care])


    def test_delit_field(self):
        self.table.add_field("компоненты", "list", "Зелёный колёса фары 67")
        self.assertDictEqual(self.table.delit_field("компоненты"),
                             self.db.all_tables()[self.test_care])
        self.assertEqual(self.table.delit_field("компоненты"), -1)

        self.assertEqual(self.table.delit_field("такого поля точно нет"), -1)

    def test_change_field(self):
        self.assertEqual(self.table.change_field("такого поля точно нет", "int", "1000000"), -1)
        self.assertEqual(self.table.change_field("цена", "int", "милион"), -1)
        self.assertEqual(self.table.change_field("двигатель", "str", "Зелёный"), -1)

        self.table.add_field("цвет", "str", "Зелёный")
        self.assertDictEqual(self.table.change_field("цвет", "str", "Красный"),
                             self.db.all_tables()[self.test_care])

        self.assertDictEqual(self.table.add_field("компоненты", "list", "колёса фары руль"),
                             self.db.all_tables()[self.test_care])



class IntegrationTestJsonDB(unittest.TestCase):
    def setUp(self):
        self.sours_on_file ='MyDB.json'
        self.test_care = "KH14470"
        self.db = JsonDB(self.sours_on_file)

    def tearDown(self):
        self.db.delete_table(self.test_care)
    def test_working_for_carepark(self):
        number_plase = 57

        old_care = self.db.carpark[str(number_plase)]
        old_carepark = self.db.all_parking_plases()
        self.db.free_up_parking_plase(str(number_plase))
        self.db.add_car_to_carepark(str(number_plase), self.test_care)
        self.db.free_up_parking_plase(str(number_plase))
        self.db.add_car_to_carepark(str(number_plase), old_care)
        new_carepark = self.db.all_parking_plases()
        self.db.delete_table(self.test_care)

        self.assertDictEqual(old_carepark, new_carepark)

    def test_working_for_tables(self):
        old_db = self.db.all_tables()
        self.db.add_table(self.test_care)
        self.db.open_table(self.test_care)
        self.db.delete_table(self.test_care)
        self.db.find_care("Красный")
        new_db = self.db.all_tables()
        self.assertDictEqual(old_db, new_db)


class IntegrationTestObjectsDB(unittest.TestCase):
    def setUp(self):
        self.sours_on_file ='MyDB.json'
        self.db = JsonDB(self.sours_on_file)
        self.test_care = "TestCareKH14472"
        self.table = self.db.add_table(self.test_care)
        with open(self.sours_on_file, 'r') as file:
            self.data = json.load(file)

    def tearDown(self):
        self.db.delete_table(self.test_care)

    def test_working_for_care(self):
        old_care = self.table.all_fields()
        self.table.add_field("компоненты", "list", "Зелёный колёса фары 67")
        self.table.change_field("компоненты", "list", "колёса фары руль")
        self.table.delit_field("компоненты")
        new_care = self.table.all_fields()
        self.assertDictEqual(old_care, new_care)


if __name__ == "__main__":
    UnitTestJsonDB.main()
    UnitTestObjectsDB.main()
    IntegrationTestJsonDB.main()
    IntegrationTestObjectsDB.main()