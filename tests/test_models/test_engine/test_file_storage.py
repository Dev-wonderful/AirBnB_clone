import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from unittest import mock


class TestFileStorage(unittest.TestCase):

    def setUp(self) -> None:
        self.fs = FileStorage()

    def test_attribute(self):
        self.assertTrue(isinstance(self.fs._FileStorage__objects, dict))
        self.assertTrue(isinstance(self.fs._FileStorage__file_path, str))

    @mock.patch('models.engine.file_storage.FileStorage.new')
    def test_new(self, mock_new):
        b1 = BaseModel()
        mock_new.assert_called_with(b1)

    @mock.patch('models.engine.file_storage.FileStorage.save')
    def test_save(self, mock_save):
        b1 = BaseModel()
        b1.name = "name"
        b1.save()
        mock_save.assert_called_with(b1)

    def test_reload(self):
        old_objs = {**self.fs.all()}
        b1 = BaseModel()
        b1.save()
        self.fs.reload()
        new_objs = {**self.fs.all()}
        self.assertNotEqual(str(old_objs), str(new_objs))
