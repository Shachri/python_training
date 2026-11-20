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
        wd.find_element(By.CSS_SELECTOR, '#LoginForm [value=Login]')

    def ensure_logout(self):
        wd = self.app.wd
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements(By.LINK_TEXT, "Logout")) > 0

    def ensure_login(self, username,password):
        wd = self.app.wd
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username,password)

    def is_logged_in_as(self,username):
        wd = self.app.wd
        return wd.find_element(By.CSS_SELECTOR,'form[name="logout"] b').text()=='('+username+')'