#!/usr/bin/python3
"""define unittests of user class"""
import os
import unittest
import models
from datetime import datetime
from time import sleep
from models.review import Review


class Test_reviewclass(unittest.TestCase):
    """ represnet unittest for testing user class"""

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
        self.assertEqual(str, type(Review().id))

    def test_createdat_type_datetype(self):
        self.assertEqual(datetime, type(Review().created_at))

    def test_updatedat_type_datetime(self):
        self.assertEqual(datetime, type(Review().updated_at))

    def test_text_str_andpublic(self):
        rev = Review()
        self.assertEqual(str, type(Review.text))
        self.assertIn("text", dir(rev))
        self.assertNotIn("text", rev.__dict__)

    def test_place_id_str_and_public(self):
        rev = Review()
        self.assertEqual(str, type(Review.place_id))
        self.assertIn("place_id", dir(rev))
        self.assertNotIn("place_id", rev.__dict__)

    def test_user_id_str_andpublic(self):
        rev = Review()
        self.assertEqual(str, type(Review.user_id))
        self.assertIn("user_id", dir(rev))
        self.assertNotIn("user_id", rev.__dict__)

    def test_str_representation(self):
        date_t = datetime.today()
        date_t_repr = repr(date_t)
        rev = Review()
        rev.id = "223355"
        rev.created_at = rev.updated_at = date_t
        rev_s = rev.__str__()
        self.assertIn("[Review] (223355)", rev_s)
        self.assertIn("'id': '223355'", rev_s)
        self.assertIn("'created_at': " + date_t_repr, rev_s)
        self.assertIn("'updated_at': " + date_t_repr, rev_s)

    def test_basic_str(self):
        rev = Review()
        self.assertTrue(str(rev).startswith('[Review]'))
        self.assertIn(rev.id, str(rev))
        self.assertIn(str(rev.__dict__), str(rev))

    def test_todict_attr_str(self):
        rev = Review()
        rev_dict = rev.to_dict()
        self.assertEqual(str, type(rev_dict["id"]))
        self.assertEqual(str, type(rev_dict["created_at"]))
        self.assertEqual(str, type(rev_dict["updated_at"]))

    def test_notnone_case(self):
        rev = Review()
        self.assertIsNotNone(rev.id)
        self.assertIsNotNone(rev.updated_at)
        self.assertIsNotNone(rev.created_at)

    def test_noinstance(self):
        self.assertEqual(Review, type(Review()))

    def test_storing_new_instance(self):
        self.assertIn(Review(), models.storage.all().values())

    def test_two_diff_id(self):
        rev_1 = Review()
        rev_2 = Review()
        self.assertNotEqual(rev_1.id, rev_2.id)

    def test_two_diff_createdat(self):
        rev_1 = Review()
        sleep(0.05)
        rev_2 = Review()
        self.assertLess(rev_1.created_at, rev_2.created_at)

    def test_two_diff_updatedat(self):
        rev_1 = Review()
        sleep(0.05)
        rev_2 = Review()
        self.assertLess(rev_1.updated_at, rev_2.updated_at)

    def test_nonearges(self):
        rev = Review(None)
        self.assertNotIn(None, rev.__dict__.values())

    def test_basic_kwargs(self):
        date_t = datetime.today()
        iformat = date_t.isoformat()
        rev = Review(id="246", created_at=iformat, updated_at=iformat)
        self.assertEqual(rev.id, "246")
        self.assertEqual(rev.created_at, date_t)
        self.assertEqual(rev.updated_at, date_t)

    def test_none_kwargs_case(self):
        with self.assertRaises(TypeError):
            Review(id=None, created_at=None, updated_at=None)

    def test_save_case_1(self):
        rev = Review()
        sleep(0.05)
        first_updated_at = rev.updated_at
        rev.save()
        self.assertLess(first_updated_at, rev.updated_at)

    def test_save_case_2(self):
        rev = Review()
        sleep(0.05)
        first_updated_at = rev.updated_at
        rev.save()
        second_updated_at = rev.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        rev.save()
        self.assertLess(second_updated_at, rev.updated_at)

    def test_save_none_arg(self):
        rev = Review()
        with self.assertRaises(TypeError):
            rev.save(None)

    def test_save_updated_files(self):
        rev = Review()
        rev.save()
        rev_id = "Review." + rev.id
        with open("file.json", "r") as file_4:
            self.assertIn(rev_id, file_4.read())

    def test_basic_todict_case(self):
        rev = Review()
        rev_dict = rev.to_dict()
        self.assertIsInstance(rev_dict, dict)

    def test_sameto_dict_type(self):
        rev = Review()
        self.assertTrue(dict, type(rev.to_dict()))

    def test_keys_to_dict(self):
        rev = Review()
        self.assertIn("id", rev.to_dict())
        self.assertIn("created_at", rev.to_dict())
        self.assertIn("updated_at", rev.to_dict())
        self.assertIn("__class__", rev.to_dict())

    def test_to_dict_with_added_attr(self):
        rev = Review()
        rev.middle_name = "reeela"
        rev.my_number = 22
        self.assertIn("reeela", rev.middle_name)
        self.assertIn("my_number", rev.to_dict())

    def test_output_of_todict(self):
        date_t = datetime.today()
        rev = Review()
        rev.id = "223355"
        rev.created_at = rev.updated_at = date_t
        tim_dict = {
            'id': '223355',
            '__class__': 'Review',
            'created_at': date_t.isoformat(),
            'updated_at': date_t.isoformat()
        }
        self.assertDictEqual(rev.to_dict(), tim_dict)

    def test_contrast_to_dict_copy_dict(self):
        rev = Review()
        self.assertNotEqual(rev.to_dict(), rev.__dict__)

    def test_to_dict_withnone_arg(self):
        rev = Review()
        with self.assertRaises(TypeError):
            rev.to_dict(None)


if __name__ == "__main__":
    unittest.main()
