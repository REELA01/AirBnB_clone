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
        dat_repr = repr(date_t)
        usr = User()
        usr.id = "223355"
        usr.created_at = usr.updated_at = date_t
        usr_s = usr.__str__()
        self.assertIn("[User] (223355)", usr_s)
        self.assertIn("'id': '223355'", usr_s)
        self.assertIn("'created_at': " + date_t_repr, usr_s)
        self.assertIn("'updated_at': " + date_t_repr, usr_s)

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


if __name__ == "__main__":
    unittest.main()
