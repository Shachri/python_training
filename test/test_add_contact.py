from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from model.contact import Contact
class test_add_contact(unittest.TestCase):


    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def logout(self, wd):
        # logout
        wd.find_element(By.LINK_TEXT, 'Logout').click()

    def return_to_home_page(self, wd):
        # return_to_home_page
        wd.get("https://localhost/addressbook/")

    def init_contact(self, wd, contact):
        # init_contact
        wd.find_element(By.CSS_SELECTOR, 'a[href="edit.php"]').click()
        wd.find_element(By.NAME, 'firstname').send_keys('%s' % contact.firstname)
        wd.find_element(By.NAME, 'middlename').send_keys('%s' % contact.middlename)
        wd.find_element(By.NAME, 'lastname').send_keys('%s' % contact.lastname)
        wd.find_element(By.NAME, 'address').send_keys('Москва')
        wd.find_element(By.CSS_SELECTOR, '[value=Enter]').click()

    def login(self, wd, username, password):
        # login
        wd.find_element(By.NAME, 'user').send_keys('%s' % username)
        wd.find_element(By.NAME, 'pass').send_keys('%s' % password)
        wd.find_element(By.CSS_SELECTOR, '#LoginForm [type=submit]').click()

    def open_home_page(self, wd):
        # open_home_page
        wd.get("https://localhost/addressbook/")

    def test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, 'admin', 'secret')
        self.init_contact(wd, Contact('Иван', 'Иванов', 'Иванович'))
        self.return_to_home_page(wd)
        self.logout(wd)

    def test_add_empty_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, 'admin', 'secret')
        self.init_contact(wd, Contact('Иван', 'Иванов', 'Иванович'))
        self.return_to_home_page(wd)
        self.logout(wd)

    def tearDown(self):
        self.wd.quit()








