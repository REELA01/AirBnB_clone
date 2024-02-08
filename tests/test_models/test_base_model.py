#!/usr/bin/python3
"""Defines unittests for models/base_model.py"""
import os
import unittest
import models
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestBaseModel_all(unittest.TestCase):
    """Unittests for testing instantiation of the BaseModel class"""

    def test_notnone_case(self):
        base_m = BaseModel()

        self.assertIsNotNone(base_m.id)
        self.assertIsNotNone(base_m.updated_at)
        self.assertIsNotNone(base_m.created_at)

    def test_noarg_case(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_objectsdict_instance(self):
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_two_diff_ids(self):
        base_m1 = BaseModel()
        base_m2 = BaseModel()
        self.assertNotEqual(base_m1.id, base_m2.id)

    def test_diff_createdat(self):
        base_m1 = BaseModel()
        sleep(0.05)
        base_m2 = BaseModel()
        self.assertLess(base_m1.created_at, base_m2.created_at)

    def test_diff_updatedat(self):
        base_m1 = BaseModel()
        sleep(0.05)
        base_m2 = BaseModel()
        self.assertLess(base_m1.updated_at, base_m2.updated_at)

    def test_str_basic_representation(self):
        date_t = datetime.today()
        dat_repr = repr(date_t)
        base_m = BaseModel()
        base_m.id = "223355"
        base_m.created_at = base_m.updated_at = date_t
        bms = base_m.__str__()
        self.assertIn("[BaseModel] (223355)", bms)
        self.assertIn("'id': '223355'", bms)
        self.assertIn("'created_at': " + dat_repr, bms)
        self.assertIn("'updated_at': " + dat_repr, bms)

    def test_args_unused(self):
        base_m = BaseModel(None)
        self.assertNotIn(None, base_m.__dict__.values())

    def test_basic_kwargs(self):
        date_t = datetime.today()
        dat_iso = date_t.isoformat()
        base_m = BaseModel(id="345", created_at=dat_iso, updated_at=dat_iso)
        self.assertEqual(base_m.id, "345")
        self.assertEqual(base_m.created_at, date_t)
        self.assertEqual(base_m.updated_at, date_t)

    def test_all_None_kwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_save_case_1(self):
        base_m = BaseModel()
        sleep(0.05)
        first_updated_at = base_m.updated_at
        base_m.save()
        self.assertLess(first_updated_at, base_m.updated_at)

    def test_save_case_2(self):
        base_m = BaseModel()
        sleep(0.05)
        first_updated_at = base_m.updated_at
        base_m.save()
        second_updated_at = base_m.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        base_m.save()
        self.assertLess(second_updated_at, base_m.updated_at)

    def test_save_withnone_arg(self):
        base_m = BaseModel()
        with self.assertRaises(TypeError):
            base_m.save(None)

    def test_save_updated_files(self):
        base_m = BaseModel()
        base_m.save()
        base_m_id = "BaseModel." + base_m.id
        with open("file.json", "r") as file_1:
            self.assertIn(base_m_id, file_1.read())

    def test_basic_todict_case(self):
        base_m = BaseModel()
        base_mdict = base_m.to_dict()
        self.assertIsInstance(base_mdict, dict)

    def test_sameto_dict_type(self):
        base_m = BaseModel()
        self.assertTrue(dict, type(base_m.to_dict()))

    def test_keys_to_dict(self):
        base_m = BaseModel()
        self.assertIn("id", base_m.to_dict())
        self.assertIn("created_at", base_m.to_dict())
        self.assertIn("updated_at", base_m.to_dict())
        self.assertIn("__class__", base_m.to_dict())

    def test_to_dict_with_added_attr(self):
        base_m = BaseModel()
        base_m.name = "reeela"
        base_m.my_number = 22
        self.assertIn("name", base_m.to_dict())
        self.assertIn("my_number", base_m.to_dict())

    def test_output_of_todict(self):
        date_t = datetime.today()
        base_m = BaseModel()
        base_m.id = "123456"
        base_m.created_at = base_m.updated_at = date_t
        tim_dict = {
            'id': '123456',
            '__class__': 'BaseModel',
            'created_at': date_t.isoformat(),
            'updated_at': date_t.isoformat()
        }
        self.assertDictEqual(base_m.to_dict(), tim_dict)

    def test_contrast_to_dict_copy_dict(self):
        base_m = BaseModel()
        self.assertNotEqual(base_m.to_dict(), base_m.__dict__)

    def test_to_dict_withnone_arg(self):
        base_m = BaseModel()
        with self.assertRaises(TypeError):
            base_m.to_dict(None)

    def test_basic_str(self):
        base_m = BaseModel()
        self.assertTrue(str(base_m).startswith('[BaseModel]'))
        self.assertIn(base_m.id, str(base_m))
        self.assertIn(str(base_m.__dict__), str(base_m))

    def test_idis_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_datetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_to_dict_datetimeatr_str(self):
        base_m = BaseModel()
        base_m_dict = base_m.to_dict()
        self.assertEqual(str, type(base_m_dict["created_at"]))
        self.assertEqual(str, type(base_m_dict["updated_at"]))

    if __name__ == "__main__":
        unittest.main()
