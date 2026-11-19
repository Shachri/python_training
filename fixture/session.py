from selenium import webdriver
from selenium.webdriver.common.by import By

class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        # login
        wd.find_element(By.CSS_SELECTOR, '#LoginForm [name=user]').send_keys('%s' % username)
        wd.find_element(By.CSS_SELECTOR, '#LoginForm [name=pass]').send_keys(password)
        wd.find_element(By.CSS_SELECTOR, '#LoginForm [value=Login]').click()

    def logout(self):
        wd = self.app.wd
        # logout
        wd.find_element(By.LINK_TEXT, "Logout").click()
        wd.find_element(By.CSS_SELECTOR, '#LoginForm [value=Login]').click()

