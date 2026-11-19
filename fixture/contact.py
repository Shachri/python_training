from selenium import webdriver
from selenium.webdriver.common.by import By

class ContactHelper:

    def __init__(self,app):
        self.app = app

    def init_contact(self, contact):
        wd = self.app.wd
        # init_contact
        wd.find_element(By.CSS_SELECTOR, 'a[href="edit.php"]').click()
        wd.find_element(By.NAME, 'firstname').send_keys('%s' % contact.firstname)
        wd.find_element(By.NAME, 'middlename').send_keys('%s' % contact.middlename)
        wd.find_element(By.NAME, 'lastname').send_keys('%s' % contact.lastname)
        wd.find_element(By.NAME, 'address').send_keys('Москва')
        wd.find_element(By.CSS_SELECTOR, '[value=Enter]').click()