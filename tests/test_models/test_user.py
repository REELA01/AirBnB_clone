#!/usr/bin/python3
"""define unittests of user class"""
import os
import unittest
import models
from datetime import datetime
from time import sleep
from models.user import User


class Test_userclass(unittest.TestCase):
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
        self.assertEqual(str, type(User().id))

    def test_createdat_type_datetype(self):
        self.assertEqual(datetime, type(User().created_at))

    def test_updatedat_type_datetime(self):
        self.assertEqual(datetime, type(User().updated_at))

    def test_email_type_str(self):
        self.assertEqual(str, type(User.email))

    def test_password_type_str(self):
        self.assertEqual(str, type(User.password))

    def test_firstname_type_str(self):
        self.assertEqual(str, type(User.first_name))

    def test_lastname_type_str(self):
        self.assertEqual(str, type(User.last_name))

    def test_str_representation(self):
        date_t = datetime.today()
        date_t_repr = repr(date_t)
        usr = User()
        usr.id = "223355"
        usr.created_at = usr.updated_at = date_t
        usr_s = usr.__str__()
        self.assertIn("[User] (223355)", usr_s)
        self.assertIn("'id': '223355'", usr_s)
        self.assertIn("'created_at': " + date_t_repr, usr_s)
        self.assertIn("'updated_at': " + date_t_repr, usr_s)

    def test_basic_str(self):
        usr = User()
        self.assertTrue(str(usr).startswith('[User]'))
        self.assertIn(usr.id, str(usr))
        self.assertIn(str(usr.__dict__), str(usr))

    def test_todict_attr_str(self):
        usr = User()
        usr_dict = usr.to_dict()
        self.assertEqual(str, type(usr_dict["id"]))
        self.assertEqual(str, type(usr_dict["created_at"]))
        self.assertEqual(str, type(usr_dict["updated_at"]))

    def test_notnone_case(self):
        usr = User()

        self.assertIsNotNone(usr.id)
        self.assertIsNotNone(usr.updated_at)
        self.assertIsNotNone(usr.created_at)

    def test_noinstance(self):
        self.assertEqual(User, type(User()))

    def test_storing_new_instance(self):
        self.assertIn(User(), models.storage.all().values())

    def test_two_diff_id(self):
        usr_1 = User()
        usr_2 = User()
        self.assertNotEqual(usr_1.id, usr_2.id)

    def test_two_diff_createdat(self):
        usr_1 = User()
        sleep(0.05)
        usr_2 = User()
        self.assertLess(usr_1.created_at, usr_2.created_at)

    def test_two_diff_updatedat(self):
        usr_1 = User()
        sleep(0.05)
        usr_2 = User()
        self.assertLess(usr_1.updated_at, usr_2.updated_at)

    def test_nonearges(self):
        usr = User(None)
        self.assertNotIn(None, usr.__dict__.values())

    def test_basic_kwargs(self):
        date_t = datetime.today()
        iformat = date_t.isoformat()
        usr = User(id="246", created_at=iformat, updated_at=iformat)
        self.assertEqual(usr.id, "246")
        self.assertEqual(usr.created_at, date_t)
        self.assertEqual(usr.updated_at, date_t)

    def test_none_kwargs_case(self):
        with self.assertRaises(TypeError):
            User(id=None, created_at=None, updated_at=None)

    def test_save_case_1(self):
        usr = User()
        sleep(0.05)
        first_updated_at = usr.updated_at
        usr.save()
        self.assertLess(first_updated_at, usr.updated_at)

    def test_save_case_2(self):
        usr = User()
        sleep(0.05)
        first_updated_at = usr.updated_at
        usr.save()
        second_updated_at = usr.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        usr.save()
        self.assertLess(second_updated_at, usr.updated_at)

    def test_save_none_arg(self):
        usr = User()
        with self.assertRaises(TypeError):
            usr.save(None)

    def test_save_updated_files(self):
        usr = User()
        usr.save()
        usr_id = "User." + usr.id
        with open("file.json", "r") as file_2:
            self.assertIn(usr_id, file_2.read())

    def test_basic_todict_case(self):
        usr = User()
        usr_dict = usr.to_dict()
        self.assertIsInstance(usr_dict, dict)

    def test_sameto_dict_type(self):
        usr = User()
        self.assertTrue(dict, type(usr.to_dict()))

    def test_keys_to_dict(self):
        usr = User()
        self.assertIn("id", usr.to_dict())
        self.assertIn("created_at", usr.to_dict())
        self.assertIn("updated_at", usr.to_dict())
        self.assertIn("__class__", usr.to_dict())

    def test_to_dict_with_added_attr(self):
        usr = User()
        usr.middle_name = "reeela"
        usr.my_number = 22
        self.assertIn("reeela", usr.middle_name)
        self.assertIn("my_number", usr.to_dict())

    def test_output_of_todict(self):
        date_t = datetime.today()
        usr = User()
        usr.id = "223355"
        usr.created_at = usr.updated_at = date_t
        tim_dict = {
            'id': '223355',
            '__class__': 'User',
            'created_at': date_t.isoformat(),
            'updated_at': date_t.isoformat()
        }
        self.assertDictEqual(usr.to_dict(), tim_dict)

    def test_contrast_to_dict_copy_dict(self):
        usr = User()
        self.assertNotEqual(usr.to_dict(), usr.__dict__)

    def test_to_dict_withnone_arg(self):
        usr = User()
        with self.assertRaises(TypeError):
            usr.to_dict(None)


if __name__ == "__main__":
    unittest.main()
