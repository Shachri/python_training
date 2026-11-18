# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from group import Group

class test_add_group(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def logout(self, wd):
        # logout
        wd.find_element(By.LINK_TEXT, "Logout").click()

    def return_to_groups_page(self, wd):
        # return to groups page
        wd.find_element(By.LINK_TEXT, "groups").click()

    def create_group(self, wd, group):
        # init group creation
        wd.find_element(By.NAME, "new").click()
        # fill group form
        wd.find_element(By.NAME, "group_name").send_keys(group.name)
        wd.find_element(By.NAME, "group_header").send_keys(group.header)
        wd.find_element(By.NAME, "group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element(By.NAME, "submit").click()

    def open_group_page(self, wd):
        # open group page
        wd.find_element(By.LINK_TEXT, "groups").click()

    def login(self, wd, username, password):
        # login
        wd.find_element(By.CSS_SELECTOR, '#LoginForm [name=user]').send_keys('%s' % username)
        wd.find_element(By.CSS_SELECTOR, '#LoginForm [name=pass]').send_keys(password)
        wd.find_element(By.CSS_SELECTOR, '#LoginForm [value=Login]').click()

    def open_home_page(self, wd):
        # open home page
        wd.get("http://localhost/addressbook/")

    def test_add_group(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, 'admin', 'secret')
        self.open_group_page(wd)
        self.create_group(wd, Group('new_group2', 'group_header', 'group_footer'))
        self.return_to_groups_page(wd)
        self.logout(wd)
        #input("Тест завершен. Нажмите Enter в консоли PyCharm, чтобы закрыть браузер...")

    def test_add_empty_group(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, 'admin', 'secret')
        self.open_group_page(wd)
        self.create_group(wd, Group('', '', ''))
        self.return_to_groups_page(wd)
        self.logout(wd)
        #input("Тест завершен. Нажмите Enter в консоли PyCharm, чтобы закрыть браузер...")

    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
