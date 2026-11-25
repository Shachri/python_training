from selenium import webdriver
from selenium.webdriver.common.by import By
from model.group import Group
from sys import maxsize


class GroupHelper:

    def __init__(self,app):
        self.app = app

    def return_to_groups_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith('group.php') and len(wd.find_elements(By.CSS_SELECTOR,'input[value="New group"]'))>0):
            wd.find_element(By.LINK_TEXT, "groups").click()

    def open_group_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith('group.php') and len(
                wd.find_elements(By.CSS_SELECTOR, 'input[value="New group"]')) > 0):
            wd.find_element(By.LINK_TEXT, "groups").click()

    def create(self, group):
        wd = self.app.wd
        self.open_group_page()
        # init group creation
        wd.find_element(By.NAME, "new").click()
        # fill group form
        self.fill_group_form(group)
        # submit group creation
        wd.find_element(By.NAME, "submit").click()
        self.return_to_groups_page()
        self.group_cache=None

    def fill_group_form(self, group):
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME, field_name).click()
            wd.find_element(By.NAME, field_name).clear()
            wd.find_element(By.NAME, field_name).send_keys(text)


    def delete(self, group):
        wd = self.app.wd
        self.open_group_page()
        # init group deletion
        wd.find_element(By.NAME, "selected[]").click()
        #submit delete
        wd.find_element(By.NAME, "delete").click()
        self.return_to_groups_page()
        self.group_cache=None

    def clear_form(self,group):
        wd = self.app.wd
        wd.find_element(By.NAME, "group_name").clear()
        wd.find_element(By.NAME, "group_header").clear()
        wd.find_element(By.NAME, "group_footer").clear()




    def modify_first_group(self, group):
        wd = self.app.wd
        self.open_group_page()
        # select first group
        wd.find_element(By.NAME, "selected[]").click()
        # open to edit
        wd.find_element(By.NAME, "edit").click()
        # fill group form
        self.fill_group_form(group)
        # save
        wd.find_element(By.NAME, "update").click()
        self.return_to_groups_page()
        self.group_cache=None

    def count(self):
        wd = self.app.wd
        self.return_to_groups_page()
        return len(wd.find_elements(By.NAME,'selected[]'))

    group_cache = None
    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_group_page()
            self.group_cache = []
            for i in wd.find_elements(By.CSS_SELECTOR,'span.group'):
                text = i.text
                id = i.find_element(By.NAME,'selected[]').get_attribute('value')
                self.group_cache.append(Group(name=text,id=id))
        return list(self.group_cache)


