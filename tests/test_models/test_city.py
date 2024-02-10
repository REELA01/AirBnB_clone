#!/usr/bin/python3
"""define unittests of cit class"""
import os
import unittest
import models
from datetime import datetime
from time import sleep
from models.city import City


class Test_cityclass(unittest.TestCase):
    """ represnet unittest for testing city class"""

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
        self.assertEqual(str, type(City().id))

    def test_createdat_type_datetype(self):
        self.assertEqual(datetime, type(City().created_at))

    def test_updatedat_type_datetime(self):
        self.assertEqual(datetime, type(City().updated_at))

    def test_name_is_public_class_attribute(self):
        cit = City()
        self.assertEqual(str, type(City.name))
        self.assertIn("name", dir(cit))
        self.assertNotIn("name", cit.__dict__)

    def test_state_id_is_public_class_attribute(self):
        cit = City()
        self.assertEqual(str, type(City.state_id))
        self.assertIn("state_id", dir(cit))
        self.assertNotIn("state_id", cit.__dict__)

    def test_str_representation(self):
        date_t = datetime.today()
        date_t_repr = repr(date_t)
        cit = City()
        cit.id = "223355"
        cit.created_at = cit.updated_at = date_t
        cit_s = cit.__str__()
        self.assertIn("[City] (223355)", cit_s)
        self.assertIn("'id': '223355'", cit_s)
        self.assertIn("'created_at': " + date_t_repr, cit_s)
        self.assertIn("'updated_at': " + date_t_repr, cit_s)

    def test_basic_str(self):
        cit = City()
        self.assertTrue(str(cit).startswith('[City]'))
        self.assertIn(cit.id, str(cit))
        self.assertIn(str(cit.__dict__), str(cit))

    def test_todict_attr_str(self):
        cit = City()
        cit_dict = cit.to_dict()
        self.assertEqual(str, type(cit_dict["id"]))
        self.assertEqual(str, type(cit_dict["created_at"]))
        self.assertEqual(str, type(cit_dict["updated_at"]))

    def test_notnone_case(self):
        cit = City()
        self.assertIsNotNone(cit.id)
        self.assertIsNotNone(cit.updated_at)
        self.assertIsNotNone(cit.created_at)

    def test_noinstance(self):
        self.assertEqual(City, type(City()))

    def test_storing_new_instance(self):
        self.assertIn(City(), models.storage.all().values())

    def test_two_diff_id(self):
        cit_1 = City()
        cit_2 = City()
        self.assertNotEqual(cit_1.id, cit_2.id)

    def test_two_diff_createdat(self):
        cit_1 = City()
        sleep(0.05)
        cit_2 = City()
        self.assertLess(cit_1.created_at, cit_2.created_at)

    def test_two_diff_updatedat(self):
        cit_1 = City()
        sleep(0.05)
        cit_2 = City()
        self.assertLess(cit_1.updated_at, cit_2.updated_at)

    def test_nonearges(self):
        cit = City(None)
        self.assertNotIn(None, cit.__dict__.values())

    def test_basic_kwargs(self):
        date_t = datetime.today()
        iformat = date_t.isoformat()
        cit = City(id="246", created_at=iformat, updated_at=iformat)
        self.assertEqual(cit.id, "246")
        self.assertEqual(cit.created_at, date_t)
        self.assertEqual(cit.updated_at, date_t)

    def test_none_kwargs_case(self):
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)

    def test_save_case_1(self):
        cit = City()
        sleep(0.05)
        first_updated_at = cit.updated_at
        cit.save()
        self.assertLess(first_updated_at, cit.updated_at)

    def test_save_case_2(self):
        cit = City()
        sleep(0.05)
        first_updated_at = cit.updated_at
        cit.save()
        second_updated_at = cit.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        cit.save()
        self.assertLess(second_updated_at, cit.updated_at)

    def test_save_none_arg(self):
        cit = City()
        with self.assertRaises(TypeError):
            cit.save(None)

    def test_save_updated_files(self):
        cit = City()
        cit.save()
        cit_id = "City." + cit.id
        with open("file.json", "r") as file_3:
            self.assertIn(cit_id, file_3.read())

    def test_basic_todict_case(self):
        cit = City()
        cit_dict = cit.to_dict()
        self.assertIsInstance(cit_dict, dict)

    def test_sameto_dict_type(self):
        cit = City()
        self.assertTrue(dict, type(cit.to_dict()))

    def test_keys_to_dict(self):
        cit = City()
        self.assertIn("id", cit.to_dict())
        self.assertIn("created_at", cit.to_dict())
        self.assertIn("updated_at", cit.to_dict())
        self.assertIn("__class__", cit.to_dict())

    def test_to_dict_with_added_attr(self):
        cit = City()
        cit.middle_name = "reeela"
        cit.my_number = 22
        self.assertIn("reeela", cit.middle_name)
        self.assertIn("my_number", cit.to_dict())

    def test_output_of_todict(self):
        date_t = datetime.today()
        cit = City()
        cit.id = "223355"
        cit.created_at = cit.updated_at = date_t
        tim_dict = {
            'id': '223355',
            '__class__': 'City',
            'created_at': date_t.isoformat(),
            'updated_at': date_t.isoformat()
        }
        self.assertDictEqual(cit.to_dict(), tim_dict)

    def test_contrast_to_dict_copy_dict(self):
        cit = City()
        self.assertNotEqual(cit.to_dict(), cit.__dict__)

    def test_to_dict_withnone_arg(self):
        cit = City()
        with self.assertRaises(TypeError):
            cit.to_dict(None)


if __name__ == "__main__":
    unittest.main()
