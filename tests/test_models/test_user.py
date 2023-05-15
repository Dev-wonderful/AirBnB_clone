import unittest
from models.user import User
from models.base_model import BaseModel
from datetime import datetime
"""" The working modules """


class TestUser(unittest.TestCase):
    """ Test for the User class"""

    def setUp(self):
        """ Set up all the methods """
        self.u1 = User()

    def test_class_attributes(self):
        u1 = User()
        attr = ["email", "password", "first_name", "last_name"]
        # getting instance attribute
        d = u1.__dict__
        for i in attr:
            # testing for class attribute
            self.assertFalse(i in d)
            self.assertTrue(hasattr(u1, i))

    def test_instance_attributes(self):
        self.assertIsInstance(self.u1.email, str)
        self.assertIsInstance(self.u1.password, str)
        self.assertIsInstance(self.u1.first_name, str)
        self.assertIsInstance(self.u1.last_name, str)
        self.assertEqual(self.u1.email, "")
        self.assertEqual(self.u1.password, "")
        self.assertEqual(self.u1.first_name, "")
        self.assertEqual(self.u1.last_name, "")

    def test_inherit_from_basemodel(self):
        self.assertTrue(issubclass(User, BaseModel))

    def tearDown(self):
        """ Tear down all method """
        pass


if __name__ == '__main__':
    unittest.main()
