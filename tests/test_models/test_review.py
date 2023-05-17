import time
import unittest
from datetime import datetime
from models.review import Review
from models.base_model import BaseModel
from unittest import mock
"""" The working modules """


class TestReview(unittest.TestCase):
    """ Test for the Review class"""

    @mock.patch('models.storage')
    def setUp(self, mock_storage):
        self.r1 = Review()
        mock_storage.new.assert_called_with(self.r1)

    def test_inherit_from_basemodel(self):
        self.assertTrue(issubclass(Review, BaseModel))

    def test_inheritance(self):
        """Test for Inheritance"""
        self.assertIsInstance(self.r1, BaseModel)
        attr_list = ['id', 'created_at', 'updated_at']
        for attr in attr_list:
            self.assertTrue(hasattr(self.r1, attr))

    def test_class_attributes(self):
        attr_list = ["place_id", "user_id", "text"]
        # getting instance attribute
        r1_dict = self.r1.__class__.__dict__
        for class_attr in attr_list:
            # testing for class attribute
            self.assertTrue(hasattr(self.r1, class_attr))
            self.assertIsInstance(r1_dict[class_attr], str)

    def test_id(self):
        r2 = Review()
        self.assertIsInstance(self.r1.id, str)
        self.assertNotEqual(self.r1.id, r2.id)

    def test_time(self):
        """Testing the time type and accuracy"""
        # r1 instance
        self.assertIsInstance(self.r1.created_at, datetime)
        self.assertIsInstance(self.r1.updated_at, datetime)
        old = self.r1.updated_at
        time.sleep(0.1)
        self.r1.save()
        new = self.r1.updated_at
        self.assertNotEqual(old, new)

    def test_str(self):
        """Testing for the correct string output"""
        # r1 instance
        output_str = "[Review] ({}) {}".format(self.r1.id,
                                               self.r1.__dict__)
        self.assertEqual(output_str, str(self.r1))

    def test_to_dict(self):
        self.assertIsInstance(self.r1.to_dict(), dict)
        r1_dict = self.r1.to_dict()
        attr_list = ['id', 'created_at', 'updated_at', '__class__']
        for attr in attr_list:
            self.assertTrue(True if attr in r1_dict else False)
        self.assertTrue(isinstance(r1_dict['created_at'], str))
        self.assertTrue(isinstance(r1_dict['updated_at'], str))
        self.assertEqual(r1_dict['__class__'], 'Review')

    @mock.patch('models.storage')
    def test_save(self, storage_mock):
        """Testing the save function"""
        self.r1.save()
        storage_mock.save.assert_called_with(self.r1)

    def tearDown(self):
        """ Tear down all method """
        pass


if __name__ == '__main__':
    unittest.main()
