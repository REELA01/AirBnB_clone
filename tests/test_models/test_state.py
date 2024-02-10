#!/usr/bin/python3
"""define unittests of state class"""
import os
import unittest
import models
from datetime import datetime
from time import sleep
from models.state import State


class Test_stateclass(unittest.TestCase):
    """ represnet unittest for testing state class"""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_idis_str(self):
        self.assertEqual(str, type(State().id))

    def test_createdat_type_datetype(self):
        self.assertEqual(datetime, type(State().created_at))

    def test_updatedat_type_datetime(self):
        self.assertEqual(datetime, type(State().updated_at))

    def test_name_str_andpuplic(self):
        stat = State()
        self.assertEqual(str, type(State.name))
        self.assertIn("name", dir(stat))
        self.assertNotIn("name", stat.__dict__)

    def test_str_representation(self):
        date_t = datetime.today()
        date_t_repr = repr(date_t)
        stat = State()
        stat.id = "223355"
        stat.created_at = stat.updated_at = date_t
        stat_s = stat.__str__()
        self.assertIn("[State] (223355)", stat_s)
        self.assertIn("'id': '223355'", stat_s)
        self.assertIn("'created_at': " + date_t_repr, stat_s)
        self.assertIn("'updated_at': " + date_t_repr, stat_s)

    def test_basic_str(self):
        stat = State()
        self.assertTrue(str(stat).startswith('[State]'))
        self.assertIn(stat.id, str(stat))
        self.assertIn(str(stat.__dict__), str(stat))

    def test_todict_attr_str(self):
        stat = State()
        stat_dict = stat.to_dict()
        self.assertEqual(str, type(stat_dict["id"]))
        self.assertEqual(str, type(stat_dict["created_at"]))
        self.assertEqual(str, type(stat_dict["updated_at"]))

    def test_notnone_case(self):
        stat = State()
        self.assertIsNotNone(stat.id)
        self.assertIsNotNone(stat.updated_at)
        self.assertIsNotNone(stat.created_at)

    def test_noinstance(self):
        self.assertEqual(State, type(State()))

    def test_storing_new_instance(self):
        self.assertIn(State(), models.storage.all().values())

    def test_two_diff_id(self):
        stat_1 = State()
        stat_2 = State()
        self.assertNotEqual(stat_1.id, stat_2.id)

    def test_two_diff_createdat(self):
        stat_1 = State()
        sleep(0.05)
        stat_2 = State()
        self.assertLess(stat_1.created_at, stat_2.created_at)

    def test_two_diff_updatedat(self):
        stat_1 = State()
        sleep(0.05)
        stat_2 = State()
        self.assertLess(stat_1.updated_at, stat_2.updated_at)

    def test_nonearges(self):
        stat = State(None)
        self.assertNotIn(None, stat.__dict__.values())

    def test_basic_kwargs(self):
        date_t = datetime.today()
        iformat = date_t.isoformat()
        stat = State(id="246", created_at=iformat, updated_at=iformat)
        self.assertEqual(stat.id, "246")
        self.assertEqual(stat.created_at, date_t)
        self.assertEqual(stat.updated_at, date_t)

    def test_none_kwargs_case(self):
        with self.assertRaises(TypeError):
            State(id=None, created_at=None, updated_at=None)

    def test_save_case_1(self):
        stat = State()
        sleep(0.05)
        first_updated_at = stat.updated_at
        stat.save()
        self.assertLess(first_updated_at, stat.updated_at)

    def test_save_case_2(self):
        stat = State()
        sleep(0.05)
        first_updated_at = stat.updated_at
        stat.save()
        second_updated_at = stat.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        stat.save()
        self.assertLess(second_updated_at, stat.updated_at)

    def test_save_none_arg(self):
        stat = State()
        with self.assertRaises(TypeError):
            stat.save(None)

    def test_save_updated_files(self):
        stat = State()
        stat.save()
        stat_id = "State." + stat.id
        with open("file.json", "r") as file_3:
            self.assertIn(stat_id, file_3.read())

    def test_basic_todict_case(self):
        stat = State()
        stat_dict = stat.to_dict()
        self.assertIsInstance(stat_dict, dict)

    def test_sameto_dict_type(self):
        stat = State()
        self.assertTrue(dict, type(stat.to_dict()))

    def test_keys_to_dict(self):
        stat = State()
        self.assertIn("id", stat.to_dict())
        self.assertIn("created_at", stat.to_dict())
        self.assertIn("updated_at", stat.to_dict())
        self.assertIn("__class__", stat.to_dict())

    def test_to_dict_with_added_attr(self):
        stat = State()
        stat.middle_name = "reeela"
        stat.my_number = 22
        self.assertIn("reeela", stat.middle_name)
        self.assertIn("my_number", stat.to_dict())

    def test_output_of_todict(self):
        date_t = datetime.today()
        stat = State()
        stat.id = "223355"
        stat.created_at = stat.updated_at = date_t
        tim_dict = {
            'id': '223355',
            '__class__': 'State',
            'created_at': date_t.isoformat(),
            'updated_at': date_t.isoformat()
        }
        self.assertDictEqual(stat.to_dict(), tim_dict)

    def test_contrast_to_dict_copy_dict(self):
        stat = State()
        self.assertNotEqual(stat.to_dict(), stat.__dict__)

    def test_to_dict_withnone_arg(self):
        stat = State()
        with self.assertRaises(TypeError):
            stat.to_dict(None)


if __name__ == "__main__":
    unittest.main()
