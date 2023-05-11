import unittest
from models.base_model import BaseModel


class Test_BaseModel(unittest.TestCase):

    def test_id(self):
        b1 = BaseModel
        self.assertTrue(b1.id)
        self.assertIsInstance(b1.id, str)


if __name__ == '__main__':
    unittest.main()
