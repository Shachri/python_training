# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest


class test_add_group(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
    def test_add_group(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd)
        self.open_group_page(wd)
        self.create_group(wd)
        self.return_to_groups_page(wd)
        self.logout(wd)
        #input("Тест завершен. Нажмите Enter в консоли PyCharm, чтобы закрыть браузер...")

    def logout(self, wd):
        # logout
        wd.find_element(By.LINK_TEXT, "Logout").click()

    def return_to_groups_page(self, wd):
        # return to groups page
        wd.find_element(By.LINK_TEXT, "groups").click()

    def create_group(self, wd):
        # init group creation
        wd.find_element(By.NAME, "new").click()
        # fill group form
        wd.find_element(By.NAME, "group_name").send_keys('new_group2')
        # submit group creation
        wd.find_element(By.NAME, "submit").click()

    def open_group_page(self, wd):
        # open group page
        wd.find_element(By.LINK_TEXT, "groups").click()

    def login(self, wd):
        # login
        wd.find_element(By.CSS_SELECTOR, '#LoginForm [name=user]').send_keys('admin')
        wd.find_element(By.CSS_SELECTOR, '#LoginForm [name=pass]').send_keys('secret')
        wd.find_element(By.CSS_SELECTOR, '#LoginForm [value=Login]').click()

    def open_home_page(self, wd):
        # open home page
        wd.get("http://localhost/addressbook/")

    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
