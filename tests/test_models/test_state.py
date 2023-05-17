import time
import unittest
from datetime import datetime
from models.state import State
from models.base_model import BaseModel
from unittest import mock
"""" The working modules """


class TestState(unittest.TestCase):
    """ Test for the State class"""

    @mock.patch('models.storage')
    def setUp(self, mock_storage):
        self.s1 = State()
        mock_storage.new.assert_called_with(self.s1)

    def test_inherit_from_basemodel(self):
        self.assertTrue(issubclass(State, BaseModel))

    def test_inheritance(self):
        """Test for Inheritance"""
        self.assertIsInstance(self.s1, BaseModel)
        attr_list = ['id', 'created_at', 'updated_at']
        for attr in attr_list:
            self.assertTrue(hasattr(self.s1, attr))

    def test_class_attributes(self):
        attr_list = ["name"]
        # getting instance attribute
        s1_dict = self.s1.__class__.__dict__
        for class_attr in attr_list:
            # testing for class attribute
            self.assertTrue(hasattr(self.s1, class_attr))
            self.assertIsInstance(s1_dict[class_attr], str)

    def test_id(self):
        s2 = State()
        self.assertIsInstance(self.s1.id, str)
        self.assertNotEqual(self.s1.id, s2.id)

    def test_time(self):
        """Testing the time type and accuracy"""
        # s1 instance
        self.assertIsInstance(self.s1.created_at, datetime)
        self.assertIsInstance(self.s1.updated_at, datetime)
        old = self.s1.updated_at
        time.sleep(0.1)
        self.s1.save()
        new = self.s1.updated_at
        self.assertNotEqual(old, new)

    def test_str(self):
        """Testing for the correct string output"""
        # s1 instance
        output_str = "[State] ({}) {}".format(self.s1.id, self.s1.__dict__)
        self.assertEqual(output_str, str(self.s1))

    def test_to_dict(self):
        self.assertIsInstance(self.s1.to_dict(), dict)
        s1_dict = self.s1.to_dict()
        attr_list = ['id', 'created_at', 'updated_at', '__class__']
        for attr in attr_list:
            self.assertTrue(True if attr in s1_dict else False)
        self.assertTrue(isinstance(s1_dict['created_at'], str))
        self.assertTrue(isinstance(s1_dict['updated_at'], str))
        self.assertEqual(s1_dict['__class__'], 'State')

    @mock.patch('models.storage')
    def test_save(self, storage_mock):
        """Testing the save function"""
        self.s1.save()
        storage_mock.save.assert_called_with(self.s1)

    def tearDown(self):
        """ Tear down all method """
        pass


if __name__ == '__main__':
    unittest.main()
