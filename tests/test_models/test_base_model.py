import unittest
from datetime import datetime
from models.base_model import BaseModel
7

class Test_BaseModel(unittest.TestCase):

    def setUp(self):
        self.b1 = BaseModel()
        self.b2 = BaseModel()

    def test_instance(self):
        self.assertIsInstance(self.b1, BaseModel)

    def test_id(self):
        self.assertTrue(hasattr(self.b1, "id"))
        self.assertIsInstance(self.b1.id, str)
        self.assertNotEqual(self.b1.id, self.b2.id)


    def test_time(self):
        self.assertTrue(hasattr(self.b1, "created_at"))
        self.assertTrue(hasattr(self.b1, "updated_at"))
        self.assertIsInstance(self.b1.created_at, datetime)
        self.assertIsInstance(self.b1.updated_at, datetime)
        self.assertEqual(self.b1.created_at, self.b1.updated_at)

    def test_save(self):
        self.b1.save()
        self.assertNotEqual(self.b1.created_at, self.b1.updated_at)

if __name__ == '__main__':
    unittest.main()
