#!/usr/bin/python3
"""define unittests of place class"""
import os
import unittest
import models
from datetime import datetime
from time import sleep
from models.place import Place


class Test_placeclass(unittest.TestCase):
    """ represnet unittest for testing place class"""

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
        self.assertEqual(str, type(Place().id))

    def test_createdat_type_datetype(self):
        self.assertEqual(datetime, type(Place().created_at))

    def test_updatedat_type_datetime(self):
        self.assertEqual(datetime, type(Place().updated_at))

    def test_name_str_andpublic(self):
        plac = Place()
        self.assertEqual(str, type(Place.name))
        self.assertIn("name", dir(plac))
        self.assertNotIn("name", plac.__dict__)

    def test_description_str_andpublic(self):
        plac = Place()
        self.assertEqual(str, type(Place.description))
        self.assertIn("description", dir(plac))
        self.assertNotIn("desctiption", plac.__dict__)

    def test_numberrooms_int_andpublic(self):
        plac = Place()
        self.assertEqual(int, type(Place.number_rooms))
        self.assertIn("number_rooms", dir(plac))
        self.assertNotIn("number_rooms", plac.__dict__)

    def test_numberbathrooms_int_public(self):
        plac = Place()
        self.assertEqual(int, type(Place.number_bathrooms))
        self.assertIn("number_bathrooms", dir(plac))
        self.assertNotIn("number_bathrooms", plac.__dict__)

    def test_maxguest_int_andpublic(self):
        plac = Place()
        self.assertEqual(int, type(Place.max_guest))
        self.assertIn("max_guest", dir(plac))
        self.assertNotIn("max_guest", plac.__dict__)

    def test_priceby_night_int_andpublic(self):
        plac = Place()
        self.assertEqual(int, type(Place.price_by_night))
        self.assertIn("price_by_night", dir(plac))
        self.assertNotIn("price_by_night", plac.__dict__)

    def test_latitude_float_andpublic(self):
        plac = Place()
        self.assertEqual(float, type(Place.latitude))
        self.assertIn("latitude", dir(plac))
        self.assertNotIn("latitude", plac.__dict__)

    def test_longitude_float_andpublic(self):
        plac = Place()
        self.assertEqual(float, type(Place.longitude))
        self.assertIn("longitude", dir(plac))
        self.assertNotIn("longitude", plac.__dict__)

    def test_amenityids_list_andpublic(self):
        plac = Place()
        self.assertEqual(list, type(Place.amenity_ids))
        self.assertIn("amenity_ids", dir(plac))
        self.assertNotIn("amenity_ids", plac.__dict__)

    def test_userid_str_andpublic(self):
        plac = Place()
        self.assertEqual(str, type(Place.user_id))
        self.assertIn("user_id", dir(plac))
        self.assertNotIn("user_id", plac.__dict__)

    def test_cityid_str_andpublic(self):
        plac = Place()
        self.assertEqual(str, type(Place.city_id))
        self.assertIn("city_id", dir(plac))
        self.assertNotIn("city_id", plac.__dict__)

    def test_str_representation(self):
        date_t = datetime.today()
        date_t_repr = repr(date_t)
        plac = Place()
        plac.id = "223355"
        plac.created_at = plac.updated_at = date_t
        plac_s = plac.__str__()
        self.assertIn("[Place] (223355)", plac_s)
        self.assertIn("'id': '223355'", plac_s)
        self.assertIn("'created_at': " + date_t_repr, plac_s)
        self.assertIn("'updated_at': " + date_t_repr, plac_s)

    def test_basic_str(self):
        plac = Place()
        self.assertTrue(str(plac).startswith('[Place]'))
        self.assertIn(plac.id, str(plac))
        self.assertIn(str(plac.__dict__), str(plac))

    def test_todict_attr_str(self):
        plac = Place()
        plac_dict = plac.to_dict()
        self.assertEqual(str, type(plac_dict["id"]))
        self.assertEqual(str, type(plac_dict["created_at"]))
        self.assertEqual(str, type(plac_dict["updated_at"]))

    def test_notnone_case(self):
        plac = Place()
        self.assertIsNotNone(plac.id)
        self.assertIsNotNone(plac.updated_at)
        self.assertIsNotNone(plac.created_at)

    def test_noinstance(self):
        self.assertEqual(Place, type(Place()))

    def test_storing_new_instance(self):
        self.assertIn(Place(), models.storage.all().values())

    def test_two_diff_id(self):
        plac_1 = Place()
        plac_2 = Place()
        self.assertNotEqual(plac_1.id, plac_2.id)

    def test_two_diff_createdat(self):
        plac_1 = Place()
        sleep(0.05)
        plac_2 = Place()
        self.assertLess(plac_1.created_at, plac_2.created_at)

    def test_two_diff_updatedat(self):
        plac_1 = Place()
        sleep(0.05)
        plac_2 = Place()
        self.assertLess(plac_1.updated_at, plac_2.updated_at)

    def test_nonearges(self):
        plac = Place(None)
        self.assertNotIn(None, plac.__dict__.values())

    def test_basic_kwargs(self):
        date_t = datetime.today()
        iformat = date_t.isoformat()
        plac = Place(id="246", created_at=iformat, updated_at=iformat)
        self.assertEqual(plac.id, "246")
        self.assertEqual(plac.created_at, date_t)
        self.assertEqual(plac.updated_at, date_t)

    def test_none_kwargs_case(self):
        with self.assertRaises(TypeError):
            Place(id=None, created_at=None, updated_at=None)

    def test_save_case_1(self):
        plac = Place()
        sleep(0.05)
        first_updated_at = plac.updated_at
        plac.save()
        self.assertLess(first_updated_at, plac.updated_at)

    def test_save_case_2(self):
        plac = Place()
        sleep(0.05)
        first_updated_at = plac.updated_at
        plac.save()
        second_updated_at = plac.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        plac.save()
        self.assertLess(second_updated_at, plac.updated_at)

    def test_save_none_arg(self):
        plac = Place()
        with self.assertRaises(TypeError):
            plac.save(None)

    def test_save_updated_files(self):
        plac = Place()
        plac.save()
        plac_id = "Place." + plac.id
        with open("file.json", "r") as file_5:
            self.assertIn(plac_id, file_5.read())

    def test_basic_todict_case(self):
        plac = Place()
        plac_dict = plac.to_dict()
        self.assertIsInstance(plac_dict, dict)

    def test_sameto_dict_type(self):
        plac = Place()
        self.assertTrue(dict, type(plac.to_dict()))

    def test_keys_to_dict(self):
        plac = Place()
        self.assertIn("id", plac.to_dict())
        self.assertIn("created_at", plac.to_dict())
        self.assertIn("updated_at", plac.to_dict())
        self.assertIn("__class__", plac.to_dict())

    def test_to_dict_with_added_attr(self):
        plac = Place()
        plac.middle_name = "reeela"
        plac.my_number = 22
        self.assertIn("reeela", plac.middle_name)
        self.assertIn("my_number", plac.to_dict())

    def test_output_of_todict(self):
        date_t = datetime.today()
        plac = Place()
        plac.id = "223355"
        plac.created_at = plac.updated_at = date_t
        tim_dict = {
            'id': '223355',
            '__class__': 'Place',
            'created_at': date_t.isoformat(),
            'updated_at': date_t.isoformat()
        }
        self.assertDictEqual(plac.to_dict(), tim_dict)

    def test_contrast_to_dict_copy_dict(self):
        plac = Place()
        self.assertNotEqual(plac.to_dict(), plac.__dict__)

    def test_to_dict_withnone_arg(self):
        plac = Place()
        with self.assertRaises(TypeError):
            plac.to_dict(None)


if __name__ == "__main__":
    unittest.main()
