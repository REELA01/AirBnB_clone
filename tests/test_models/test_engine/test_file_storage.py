#!/usr/bin/python3
"""define unittests for filestorage"""
import os
import unittest
import json
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class Test_FileStorage_cases(unittest.TestCase):
    """Unittests for testing filestorage"""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove('file.json')
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_empty_filestorage(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_noarg_filestorage(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_intilization(self):
        self.assertEqual(type(models.storage), FileStorage)

    def test_filepath_is_str(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_objects_is_dict(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_all_case_1(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_all_empty(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new_case_1(self):
        base_m = BaseModel()
        models.storage.new(base_m)
        self.assertIn("BaseModel." + base_m.id, models.storage.all().keys())
        self.assertIn(base_m, models.storage.all().values())

    def test_new_empty_args(self):
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_save_case_1(self):
        models.storage.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_save_empty_arg(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload_case_1(self):
        base_m = BaseModel()
        models.storage.reload()
        for o in models.storage.all().values():
            val = o
        self.assertEqual(base_m.to_dict()['id'], val.to_dict()['id'])

    def test_reload_empty_arg(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()
