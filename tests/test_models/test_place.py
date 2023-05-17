import time
import unittest
from datetime import datetime
from models.place import Place
from models.base_model import BaseModel
from unittest import mock
"""" The working modules """


class TestUser(unittest.TestCase):
    """ Test for the User class"""

    @mock.patch('models.storage')
    def setUp(self, mock_storage):
        self.p1 = Place()
        mock_storage.new.assert_called_with(self.p1)

    def test_inherit_from_basemodel(self):
        self.assertTrue(issubclass(Place, BaseModel))

    def test_inheritance(self):
        """Test for Inheritance"""
        self.assertIsInstance(self.p1, BaseModel)
        attr_list = ['id', 'created_at', 'updated_at']
        for attr in attr_list:
            self.assertTrue(hasattr(self.p1, attr))

    def test_class_attributes(self):
        attr_list_str = ["name", "city_id", "user_id", "description"]
        attr_list_int = ["number_rooms",
                         "number_bathrooms",
                         "max_guest",
                         "price_by_night"]
        attr_list_float = ["latitude", "longitude"]
        attr_list_list = ["amenity_ids"]
        # getting instance attribute
        p1_dict = self.p1.__class__.__dict__
        for class_attr in attr_list_str:
            # testing for class attribute
            self.assertTrue(hasattr(self.p1, class_attr))
            self.assertIsInstance(p1_dict[class_attr], str)
        for class_attr in attr_list_int:
            # testing for class attribute
            self.assertTrue(hasattr(self.p1, class_attr))
            self.assertIsInstance(p1_dict[class_attr], int)
        for class_attr in attr_list_float:
            # testing for class attribute
            self.assertTrue(hasattr(self.p1, class_attr))
            self.assertIsInstance(p1_dict[class_attr], float)
        for class_attr in attr_list_list:
            # testing for class attribute
            self.assertTrue(hasattr(self.p1, class_attr))
            self.assertIsInstance(p1_dict[class_attr], list)

    def test_id(self):
        p2 = Place()
        self.assertIsInstance(self.p1.id, str)
        self.assertNotEqual(self.p1.id, p2.id)

    def test_time(self):
        """Testing the time type and accuracy"""
        # p1 instance
        self.assertIsInstance(self.p1.created_at, datetime)
        self.assertIsInstance(self.p1.updated_at, datetime)
        self.assertAlmostEqual(self.p1.created_at, self.p1.updated_at)
        old = self.p1.updated_at
        time.sleep(0.1)
        self.p1.save()
        new = self.p1.updated_at
        self.assertNotEqual(old, new)

    def test_str(self):
        """Testing for the correct string output"""
        # p1 instance
        output_str = "[Place] ({}) {}".format(self.p1.id, self.p1.__dict__)
        self.assertEqual(output_str, str(self.p1))

    def test_to_dict(self):
        self.assertIsInstance(self.p1.to_dict(), dict)
        p1_dict = self.p1.to_dict()
        attr_list = ['id', 'created_at', 'updated_at', '__class__']
        for attr in attr_list:
            self.assertTrue(True if attr in p1_dict else False)
        self.assertTrue(isinstance(p1_dict['created_at'], str))
        self.assertTrue(isinstance(p1_dict['updated_at'], str))
        self.assertEqual(p1_dict['__class__'], 'Place')

    @mock.patch('models.storage')
    def test_save(self, storage_mock):
        """Testing the save function"""
        self.p1.save()
        storage_mock.save.assert_called_with(self.p1)

    def tearDown(self):
        """ Tear down all method """
        pass


if __name__ == '__main__':
    unittest.main()
