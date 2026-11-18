# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from group import Group
from application import Application

class test_add_group(unittest.TestCase):
    def setUp(self):
        self.app = Application()

    def test_add_group(self):
        self.app.login('admin', 'secret')
        self.app.create_group(Group('new_group2', 'group_header', 'group_footer'))
        self.app.logout()

    def test_add_empty_group(self):
        self.app.login('admin', 'secret')
        self.app.create_group(Group('', '', ''))
        self.app.logout()

    def tearDown(self):
        self.app.destroy()

if __name__ == "__main__":
    unittest.main()
