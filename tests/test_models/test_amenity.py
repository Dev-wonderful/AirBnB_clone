import time
import unittest
from datetime import datetime
from models.amenity import Amenity
from models.base_model import BaseModel
from unittest import mock
"""" The working modules """


class TestAmenity(unittest.TestCase):
    """ Test for the User class"""

    @mock.patch('models.storage')
    def setUp(self, mock_storage):
        self.a1 = Amenity()
        mock_storage.new.assert_called_with(self.a1)

    def test_inherit_from_basemodel(self):
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_inheritance(self):
        """Test for Inheritance"""
        self.assertIsInstance(self.a1, BaseModel)
        attr_list = ['id', 'created_at', 'updated_at']
        for attr in attr_list:
            self.assertTrue(hasattr(self.a1, attr))

    def test_class_attributes(self):
        attr_list = ["name"]
        # getting instance attribute
        a1_dict = self.a1.__dict__
        for class_attr in attr_list:
            # testing for class attribute
            self.assertFalse(class_attr in a1_dict)
            self.assertTrue(hasattr(self.a1, class_attr))
            self.assertIsInstance(class_attr, str)

    def test_id(self):
        a2 = Amenity()
        self.assertIsInstance(self.a1.id, str)
        self.assertNotEqual(self.a1.id, a2.id)

    def test_time(self):
        """Testing the time type and accuracy"""
        # a1 instance
        self.assertIsInstance(self.a1.created_at, datetime)
        self.assertIsInstance(self.a1.updated_at, datetime)
        old = self.a1.updated_at
        time.sleep(0.1)
        self.a1.save()
        new = self.a1.updated_at
        self.assertNotEqual(old, new)

    def test_str(self):
        """Testing for the correct string output"""
        # a1 instance
        output_str = "[Amenity] ({}) {}".format(self.a1.id, self.a1.__dict__)
        self.assertEqual(output_str, str(self.a1))

    def test_to_dict(self):
        self.assertIsInstance(self.a1.to_dict(), dict)
        a1_dict = self.a1.to_dict()
        attr_list = ['id', 'created_at', 'updated_at', '__class__']
        for attr in attr_list:
            self.assertTrue(True if attr in a1_dict else False)
        self.assertTrue(isinstance(a1_dict['created_at'], str))
        self.assertTrue(isinstance(a1_dict['updated_at'], str))
        self.assertEqual(a1_dict['__class__'], 'Amenity')

    @mock.patch('models.storage')
    def test_save(self, storage_mock):
        """Testing the save function"""
        self.a1.save()
        storage_mock.save.assert_called_with(self.a1)

    def tearDown(self):
        """ Tear down all method """
        pass


if __name__ == '__main__':
    unittest.main()
