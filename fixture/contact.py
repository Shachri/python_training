from selenium import webdriver
from selenium.webdriver.common.by import By
from model.contact import Contact
import re


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def return_to_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith('addressbook/') and len(
                wd.find_elements(By.XPATH, 'a[contains(text(),"Last name")]')) > 0):
            wd.find_element(By.LINK_TEXT, 'home').click()

    def init_contact(self, contact):
        wd = self.app.wd
        # init_contact
        wd.find_element(By.CSS_SELECTOR, 'a[href="edit.php"]').click()
        #fill_contact_form
        self.fill_contact_form(contact, wd)
        wd.find_element(By.CSS_SELECTOR, '[value=Enter]').click()
        self.contact_cache = None

    def fill_contact_form(self, contact, wd):
        wd.find_element(By.NAME, 'firstname').send_keys('%s' % contact.firstname)
        wd.find_element(By.NAME, 'middlename').send_keys('%s' % contact.middlename)
        wd.find_element(By.NAME, 'lastname').send_keys('%s' % contact.lastname)
        wd.find_element(By.NAME, 'address').send_keys('Москва')

    def clear_form(self, contact, wd):
        wd.find_element(By.NAME, 'firstname').clear()
        wd.find_element(By.NAME, 'middlename').clear()
        wd.find_element(By.NAME, 'lastname').clear()
        wd.find_element(By.NAME, 'address').clear()

    def edit(self, contact, index):
        wd = self.app.wd
        self.edit_by_index(contact, 0)

    def edit_by_index(self, contact, index):
        wd = self.app.wd
        # init_contact
        self.return_to_home_page()
        self.select_contact(index)
        self.clear_form(contact, wd)
        self.fill_contact_form(contact, wd)
        wd.find_element(By.NAME, 'update').click()
        self.return_to_home_page()
        self.contact_cache = None

    def select_contact_for_edit(self, index):
        wd = self.app.wd
        wd.find_elements(By.NAME, 'selected[]')[index].click()
        wd.find_elements(By.CSS_SELECTOR, 'a [title="Edit"]')[index].click()

    def delete(self):
        wd = self.app.wd
        self.return_to_home_page()
        self.delete_by_index(0)
        self.return_to_home_page()
        self.contact_cache = None

    def delete_by_index(self, index):
        wd = self.app.wd
        self.return_to_home_page()
        wd.find_elements(By.NAME, 'selected[]')[index].click()
        wd.find_element(By.NAME, 'delete').click()
        self.return_to_home_page()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.return_to_home_page()
        return len(wd.find_elements(By.NAME, 'selected[]'))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.return_to_home_page()
            self.contact_cache = []
            for elements in wd.find_elements(By.NAME, 'entry'):
                cells = elements.find_elements(By.TAG_NAME, 'td')
                firstname = cells[2].text
                lastname = cells[1].text
                id = cells[0].find_element(By.TAG_NAME, 'input').get_attribute('value')
                address = cells[3].text
                all_emails = cells[4].text
                all_phones = cells[5].text
                self.contact_cache.append(
                    Contact(firstname=firstname, middlename=None, lastname=lastname, address=address, id=id,
                            all_phones_from_home_page=all_phones, all_emails_from_home_page=all_emails))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.return_to_home_page()
        self.select_contact_for_edit(index)
        firsname = wd.find_element(By.NAME, 'firstname').get_attribute('value')
        lastname = wd.find_element(By.NAME, 'lastname').get_attribute('value')
        middlename = wd.find_element(By.NAME, 'middlename').get_attribute('value')
        id = wd.find_element(By.NAME, 'id').get_attribute('value')
        homephone = wd.find_element(By.NAME, 'home').get_attribute('value')
        mobilephone = wd.find_element(By.NAME, 'mobile').get_attribute('value')
        workphone = wd.find_element(By.NAME, 'work').get_attribute('value')
        email = wd.find_element(By.NAME, 'email').get_attribute('value')
        email2 = wd.find_element(By.NAME, 'email2').get_attribute('value')
        email3 = wd.find_element(By.NAME, 'email3').get_attribute('value')
        address = wd.find_element(By.NAME, 'address').get_attribute('value')
        return Contact(firstname=firsname, lastname=lastname, middlename=middlename, id=id, homephone=homephone,
                       mobilephone=mobilephone, workphone=workphone,email=email, email2=email2,email3=email3,
                       address=address)

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.return_to_home_page()
        row = wd.find_elements(By.NAME, 'entry')[index]
        cells = wd.find_elements(By.TAG_NAME, 'td')[6]
        cells.find_element(By.TAG_NAME, 'a').click()

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element(By.ID, 'content').text
        homephone = re.search('H: (.*)',text).group(1)
        mobilephone = re.search('M: (.*)',text).group(1)
        workphone = re.search('W: (.*)',text).group(1)
        return Contact(homephone=homephone,mobilephone=mobilephone, workphone=workphone)


