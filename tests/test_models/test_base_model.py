import unittest
from datetime import datetime
from models.base_model import BaseModel
from unittest import mock
import time
""" Working modules"""


class TestBaseModel(unittest.TestCase):

    @mock.patch('models.storage')
    def setUp(self, mock_storage):
        self.b1 = BaseModel()
        mock_storage.new.assert_called()
        self.b2 = BaseModel()
        mock_storage.new.assert_called()

    def test_instance(self):
        """Test for the instance of the parent class"""
        self.assertIsInstance(self.b1, BaseModel)
        self.assertIsInstance(self.b2, BaseModel)
        attr_list = ['id', 'created_at', 'updated_at']
        for attr in attr_list:
            self.assertTrue(hasattr(self.b1, attr))
            self.assertTrue(hasattr(self.b2, attr))

    def test_id(self):
        self.assertIsInstance(self.b1.id, str)
        self.assertIsInstance(self.b2.id, str)
        self.assertNotEqual(self.b1.id, self.b2.id)

    def test_time(self):
        """Testing the time type and accuracy"""
        # b1 instance
        self.assertIsInstance(self.b1.created_at, datetime)
        self.assertIsInstance(self.b1.updated_at, datetime)
        self.assertAlmostEqual(self.b1.created_at, self.b1.updated_at)
        old = self.b1.updated_at
        time.sleep(0.1)
        self.b1.save()
        new = self.b1.updated_at
        self.assertNotEqual(old, new)
        # b2 instance
        self.assertIsInstance(self.b2.created_at, datetime)
        self.assertIsInstance(self.b2.updated_at, datetime)
        self.assertAlmostEqual(self.b2.created_at, self.b2.updated_at)
        old = self.b2.updated_at
        time.sleep(0.1)
        self.b2.save()
        new = self.b2.updated_at
        self.assertNotEqual(old, new)

    def test_str(self):
        """Testing for the correct string output"""
        # b1 instance
        output_str = "[BaseModel] ({}) {}".format(self.b1.id,
                                                  self.b1.__dict__)
        self.assertEqual(output_str, str(self.b1))
        # b2 instance
        output_str = "[BaseModel] ({}) {}".format(self.b2.id,
                                                  self.b2.__dict__)
        self.assertEqual(output_str, str(self.b2))

    def test_to_dict(self):
        self.assertIsInstance(self.b1.to_dict(), dict)
        self.assertIsInstance(self.b2.to_dict(), dict)
        b1_dict = self.b1.to_dict()
        b2_dict = self.b2.to_dict()
        attr_list = ['id', 'created_at', 'updated_at', '__class__']
        for attr in attr_list:
            self.assertTrue(True if attr in b1_dict else False)
            self.assertTrue(b2_dict.get(attr))
        self.assertTrue(isinstance(b1_dict['created_at'], str))
        self.assertTrue(isinstance(b1_dict['updated_at'], str))
        self.assertEqual(b1_dict['__class__'], 'BaseModel')
        self.assertTrue(isinstance(b2_dict['created_at'], str))
        self.assertTrue(isinstance(b2_dict['updated_at'], str))
        self.assertEqual(b2_dict['__class__'], 'BaseModel')

    @mock.patch('models.storage')
    def test_save(self, storage_mock):
        """Testing the save function"""
        self.b1.save()
        storage_mock.save.assert_called()
        self.b2.save()
        storage_mock.save.assert_called_with(self.b2)


if __name__ == '__main__':
    unittest.main()
