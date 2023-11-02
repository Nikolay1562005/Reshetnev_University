import unittest

from Lab2_in_OOP_style import JsonDB, ObjectsDB

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.db = JsonDB('MyDB.json')

    # def test_open_table(self):
    #     self.assertEquals(str(self.db.open_table("KH14472")), "KH14472")
    #
    # def test_delit_table(self):
    #     self.assertEquals(self.db.delete_table("KH14472"), "Успешно удалена таблица KH14472")

    def test_add_table(self):
        
        self.assertEquals(str(self.db.add_table("KH14472")), "KH14472")


if __name__ == "__main__":
    unittest.main()