import time
import unittest
from datetime import datetime
from models.user import User
from models.base_model import BaseModel
from unittest import mock
"""" The working modules """


class TestUser(unittest.TestCase):
    """ Test for the User class"""

    @mock.patch('models.storage')
    def setUp(self, mock_storage):
        self.u1 = User()
        mock_storage.new.assert_called_with(self.u1)

    def test_inherit_from_basemodel(self):
        self.assertTrue(issubclass(User, BaseModel))

    def test_inheritance(self):
        """Test for Inheritance"""
        self.assertIsInstance(self.u1, BaseModel)
        attr_list = ['id', 'created_at', 'updated_at']
        for attr in attr_list:
            self.assertTrue(hasattr(self.u1, attr))

    def test_class_attributes(self):
        u1 = User()
        attr_list = ["email", "password", "first_name", "last_name"]
        # getting instance attribute
        d = u1.__dict__
        for class_attr in attr_list:
            # testing for class attribute
            self.assertFalse(class_attr in d)
            self.assertTrue(hasattr(u1, class_attr))
            self.assertIsInstance(class_attr, str)

    def test_id(self):
        u2 = User()
        self.assertIsInstance(self.u1.id, str)
        self.assertNotEqual(self.u1.id, u2.id)

    def test_time(self):
        """Testing the time type and accuracy"""
        # u1 instance
        self.assertIsInstance(self.u1.created_at, datetime)
        self.assertIsInstance(self.u1.updated_at, datetime)
        self.assertAlmostEqual(self.u1.created_at, self.u1.updated_at)
        old = self.u1.updated_at
        time.sleep(0.1)
        self.u1.save()
        new = self.u1.updated_at
        self.assertNotEqual(old, new)

    def test_str(self):
        """Testing for the correct string output"""
        # u1 instance
        output_str = "[User] ({}) {}".format(self.u1.id, self.u1.__dict__)
        self.assertEqual(output_str, str(self.u1))

    def test_to_dict(self):
        self.assertIsInstance(self.u1.to_dict(), dict)
        u1_dict = self.u1.to_dict()
        attr_list = ['id', 'created_at', 'updated_at', '__class__']
        for attr in attr_list:
            self.assertTrue(True if attr in u1_dict else False)
        self.assertTrue(isinstance(u1_dict['created_at'], str))
        self.assertTrue(isinstance(u1_dict['updated_at'], str))
        self.assertEqual(u1_dict['__class__'], 'User')

    @mock.patch('models.storage')
    def test_save(self, storage_mock):
        """Testing the save function"""
        self.u1.save()
        storage_mock.save.assert_called_with(self.u1)

    def tearDown(self):
        """ Tear down all method """
        pass


if __name__ == '__main__':
    unittest.main()
