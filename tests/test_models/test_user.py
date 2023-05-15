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
        d = u1.__dict__
        for i in attr:
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
        self.assertTrue(issubclass(self.u1, BaseModel))

    def tearDown(self):
        """ Tear down all method """
        pass


class TestInstance(unittest.TestCase):
    """ Test for the instance of the parent class """

    def setup(self):
        """ Set up all Methods """
        self.b1 = BaseModel()
        self.b2 = BaseModel()

    def test_instance(self):
        """ Test for the instance of the parent class """

        self.assertIsInstance(self.b1, BaseModel)

    def test_instance_attributes(self):
        """ Test for instance attributes of the parent class """
        self.assertTrue(hasattr(self.b1, "id"))
        self.assertIsInstance(self.b1, str)
        self.assertNotEqual(self.b1.id, self.b2.id)

    def tearDown(self):
        """ Tear down all methods """
        pass


class TestTime(unittest.TestCase):
    """ Test to check the accuracy of the time """

    def setUp(self):
        self.b1 = BaseModel()

    def test_accurate_time(self):
        self.assertTrue(hasattr(self.b1, "created_at"))
        self.assertTrue(hasattr(self.b1, "updated_at"))
        self.assertIsInstance(self.b1.created_at, datetime)
        self.assertIsInstance(self.b1.updated_at, datetime)
        self.assertNotEqual(self.b1.created_at, self.b1.updated_at)

    def tearDown(self):
        """ Tear down all methods """
        pass


class TestSave(unittest.TestCase):
    """ Test for checking time that objects are updated """

    def setUp(self):
        self.b1 = BaseModel()

    def test_save(self):
        """ The test to save update time """
        self.b1.save()
        self.assertNotEqual(self.b1.created_at, self.b1.updated_at)

    def tearDown(self):
        """ Tear down all methods """
        pass


class TestToDict(unittest.TestCase):

    def setUp(self):
        self.b1 = BaseModel()

    def test_to_dict(self):
        self.assertIsInstance(self.b1.to_dict(), dict)


if __name__ == '__main__':
    unittest.main()
