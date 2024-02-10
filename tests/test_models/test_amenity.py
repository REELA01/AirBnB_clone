#!/usr/bin/python3
"""define unittests of amenity class"""
import os
import unittest
import models
from datetime import datetime
from time import sleep
from models.amenity import Amenity


class Test_amenityclass(unittest.TestCase):
    """ represnet unittest for testing amenity class"""

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
        self.assertEqual(str, type(Amenity().id))

    def test_createdat_type_datetype(self):
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_updatedat_type_datetime(self):
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_name_str_andpublic(self):
        amen = Amenity()
        self.assertEqual(str, type(Amenity.name))
        self.assertIn("name", dir(Amenity()))
        self.assertNotIn("name", amen.__dict__)

    def test_str_representation(self):
        date_t = datetime.today()
        date_t_repr = repr(date_t)
        amen = Amenity()
        amen.id = "223355"
        amen.created_at = amen.updated_at = date_t
        amen_s = amen.__str__()
        self.assertIn("[Amenity] (223355)", amen_s)
        self.assertIn("'id': '223355'", amen_s)
        self.assertIn("'created_at': " + date_t_repr, amen_s)
        self.assertIn("'updated_at': " + date_t_repr, amen_s)

    def test_basic_str(self):
        amen = Amenity()
        self.assertTrue(str(amen).startswith('[Amenity]'))
        self.assertIn(amen.id, str(amen))
        self.assertIn(str(amen.__dict__), str(amen))

    def test_todict_attr_str(self):
        amen = Amenity()
        amen_dict = amen.to_dict()
        self.assertEqual(str, type(amen_dict["id"]))
        self.assertEqual(str, type(amen_dict["created_at"]))
        self.assertEqual(str, type(amen_dict["updated_at"]))

    def test_notnone_case(self):
        amen = Amenity()
        self.assertIsNotNone(amen.id)
        self.assertIsNotNone(amen.updated_at)
        self.assertIsNotNone(amen.created_at)

    def test_noinstance(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_storing_new_instance(self):
        self.assertIn(Amenity(), models.storage.all().values())

    def test_two_diff_id(self):
        amen_1 = Amenity()
        amen_2 = Amenity()
        self.assertNotEqual(amen_1.id, amen_2.id)

    def test_two_diff_createdat(self):
        amen_1 = Amenity()
        sleep(0.05)
        amen_2 = Amenity()
        self.assertLess(amen_1.created_at, amen_2.created_at)

    def test_two_diff_updatedat(self):
        amen_1 = Amenity()
        sleep(0.05)
        amen_2 = Amenity()
        self.assertLess(amen_1.updated_at, amen_2.updated_at)

    def test_nonearges(self):
        amen = Amenity(None)
        self.assertNotIn(None, amen.__dict__.values())

    def test_basic_kwargs(self):
        date_t = datetime.today()
        iformat = date_t.isoformat()
        amen = Amenity(id="246", created_at=iformat, updated_at=iformat)
        self.assertEqual(amen.id, "246")
        self.assertEqual(amen.created_at, date_t)
        self.assertEqual(amen.updated_at, date_t)

    def test_none_kwargs_case(self):
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)

    def test_save_case_1(self):
        amen = Amenity()
        sleep(0.05)
        first_updated_at = amen.updated_at
        amen.save()
        self.assertLess(first_updated_at, amen.updated_at)

    def test_save_case_2(self):
        amen = Amenity()
        sleep(0.05)
        first_updated_at = amen.updated_at
        amen.save()
        second_updated_at = amen.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        amen.save()
        self.assertLess(second_updated_at, amen.updated_at)

    def test_save_none_arg(self):
        amen = Amenity()
        with self.assertRaises(TypeError):
            amen.save(None)

    def test_save_updated_files(self):
        amen = Amenity()
        amen.save()
        amen_id = "Amenity." + amen.id
        with open("file.json", "r") as file_6:
            self.assertIn(amen_id, file_6.read())

    def test_basic_todict_case(self):
        amen = Amenity()
        amen_dict = amen.to_dict()
        self.assertIsInstance(amen_dict, dict)

    def test_sameto_dict_type(self):
        amen = Amenity()
        self.assertTrue(dict, type(amen.to_dict()))

    def test_keys_to_dict(self):
        amen = Amenity()
        self.assertIn("id", amen.to_dict())
        self.assertIn("created_at", amen.to_dict())
        self.assertIn("updated_at", amen.to_dict())
        self.assertIn("__class__", amen.to_dict())

    def test_to_dict_with_added_attr(self):
        amen = Amenity()
        amen.middle_name = "reeela"
        amen.my_number = 22
        self.assertIn("reeela", amen.middle_name)
        self.assertIn("my_number", amen.to_dict())

    def test_output_of_todict(self):
        date_t = datetime.today()
        amen = Amenity()
        amen.id = "223355"
        amen.created_at = amen.updated_at = date_t
        tim_dict = {
            'id': '223355',
            '__class__': 'Amenity',
            'created_at': date_t.isoformat(),
            'updated_at': date_t.isoformat()
        }
        self.assertDictEqual(amen.to_dict(), tim_dict)

    def test_contrast_to_dict_copy_dict(self):
        amen = Amenity()
        self.assertNotEqual(amen.to_dict(), amen.__dict__)

    def test_to_dict_withnone_arg(self):
        amen = Amenity()
        with self.assertRaises(TypeError):
            amen.to_dict(None)


if __name__ == "__main__":
    unittest.main()
