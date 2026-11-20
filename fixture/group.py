from selenium import webdriver
from selenium.webdriver.common.by import By


class GroupHelper:

    def __init__(self,app):
        self.app = app

    def return_to_groups_page(self):
        wd = self.app.wd
        # return to groups page
        wd.find_element(By.LINK_TEXT, "groups").click()

    def open_group_page(self):
        wd = self.app.wd
        # open group page
        wd.find_element(By.LINK_TEXT, "groups").click()

    def create(self, group):
        wd = self.app.wd
        self.open_group_page()
        # init group creation
        wd.find_element(By.NAME, "new").click()
        # fill group form
        self.fill_group_form(group, wd)
        # submit group creation
        wd.find_element(By.NAME, "submit").click()
        self.return_to_groups_page()

    def fill_group_form(self, group, wd):
        wd.find_element(By.NAME, "group_name").send_keys(group.name)
        wd.find_element(By.NAME, "group_header").send_keys(group.header)
        wd.find_element(By.NAME, "group_footer").send_keys(group.footer)

    def delete(self, group):
        wd = self.app.wd
        self.open_group_page()
        # init group deletion
        wd.find_element(By.NAME, "selected[]").click()
        #submit delete
        wd.find_element(By.NAME, "delete").click()
        self.return_to_groups_page()

    def clear_form(self,group):
        wd = self.app.wd
        wd.find_element(By.NAME, "group_name").clear()
        wd.find_element(By.NAME, "group_header").clear()
        wd.find_element(By.NAME, "group_footer").clear()




    def edit(self, group):
        wd = self.app.wd
        self.open_group_page()
        # init group deletion
        wd.find_element(By.NAME, "selected[]").click()
        #open_to_edit
        wd.find_element(By.NAME, "edit").click()
        self.clear_form(group)
        self.fill_group_form(group, wd)
        #save
        wd.find_element(By.NAME, "update").click()
        self.return_to_groups_page()

    def count(self):
        wd = self.app.wd
        self.return_to_groups_page()
        return len(wd.find_elements(By.NAME,'selected[]'))
