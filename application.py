from selenium import webdriver
from selenium.webdriver.common.by import By


class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def logout(self):
        wd = self.wd
        # logout
        wd.find_element(By.LINK_TEXT, "Logout").click()

    def return_to_groups_page(self):
        wd = self.wd
        # return to groups page
        wd.find_element(By.LINK_TEXT, "groups").click()

    def create_group(self, group):
        wd = self.wd
        self.open_group_page()
        # init group creation
        wd.find_element(By.NAME, "new").click()
        # fill group form
        wd.find_element(By.NAME, "group_name").send_keys(group.name)
        wd.find_element(By.NAME, "group_header").send_keys(group.header)
        wd.find_element(By.NAME, "group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element(By.NAME, "submit").click()
        self.return_to_groups_page()

    def open_group_page(self):
        wd = self.wd
        # open group page
        wd.find_element(By.LINK_TEXT, "groups").click()

    def login(self, username, password):
        wd = self.wd
        self.open_home_page()
        # login
        wd.find_element(By.CSS_SELECTOR, '#LoginForm [name=user]').send_keys('%s' % username)
        wd.find_element(By.CSS_SELECTOR, '#LoginForm [name=pass]').send_keys(password)
        wd.find_element(By.CSS_SELECTOR, '#LoginForm [value=Login]').click()

    def open_home_page(self):
        wd = self.wd
        # open home page
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()