import time
import unittest
from datetime import datetime
from models.city import City
# from models.state import State
from models.base_model import BaseModel
from unittest import mock
"""" The working modules """


class TestUser(unittest.TestCase):
    """ Test for the User class"""

    @mock.patch('models.storage')
    def setUp(self, mock_storage):
        self.c1 = City()
        mock_storage.new.assert_called_with(self.c1)

    def test_inherit_from_basemodel(self):
        self.assertTrue(issubclass(City, BaseModel))

    def test_inheritance(self):
        """Test for Inheritance"""
        self.assertIsInstance(self.c1, BaseModel)
        attr_list = ['id', 'created_at', 'updated_at']
        for attr in attr_list:
            self.assertTrue(hasattr(self.c1, attr))

    def test_class_attributes(self):
        # state = State()
        # self.c1.name = "City Name"
        # self.c1.state_id = state.id
        attr_list = ["name", "state_id"]
        # getting instance attribute
        c1_dict = self.c1.__class__.__dict__
        for class_attr in attr_list:
            # testing for class attribute
            # self.assertFalse(class_attr in c1_dict)
            self.assertTrue(hasattr(self.c1, class_attr))
            self.assertIsInstance(c1_dict[class_attr], str)

    def test_id(self):
        c2 = City()
        self.assertIsInstance(self.c1.id, str)
        self.assertNotEqual(self.c1.id, c2.id)

    def test_time(self):
        """Testing the time type and accuracy"""
        # c1 instance
        self.assertIsInstance(self.c1.created_at, datetime)
        self.assertIsInstance(self.c1.updated_at, datetime)
        self.assertAlmostEqual(self.c1.created_at, self.c1.updated_at)
        old = self.c1.updated_at
        time.sleep(0.1)
        self.c1.save()
        new = self.c1.updated_at
        self.assertNotEqual(old, new)

    def test_str(self):
        """Testing for the correct string output"""
        # c1 instance
        output_str = "[City] ({}) {}".format(self.c1.id, self.c1.__dict__)
        self.assertEqual(output_str, str(self.c1))

    def test_to_dict(self):
        self.assertIsInstance(self.c1.to_dict(), dict)
        c1_dict = self.c1.to_dict()
        attr_list = ['id', 'created_at', 'updated_at', '__class__']
        for attr in attr_list:
            self.assertTrue(True if attr in c1_dict else False)
        self.assertTrue(isinstance(c1_dict['created_at'], str))
        self.assertTrue(isinstance(c1_dict['updated_at'], str))
        self.assertEqual(c1_dict['__class__'], 'City')

    @mock.patch('models.storage')
    def test_save(self, storage_mock):
        """Testing the save function"""
        self.c1.save()
        storage_mock.save.assert_called_with(self.c1)

    def tearDown(self):
        """ Tear down all method """
        pass


if __name__ == '__main__':
    unittest.main()
