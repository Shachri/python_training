from selenium import webdriver
from selenium.webdriver.common.by import By
from model.contact import Contact


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

    def edit(self, contact):
        wd = self.app.wd
        # init_contact
        self.return_to_home_page()
        wd.find_element(By.NAME, 'selected[]').click()
        wd.find_element(By.CSS_SELECTOR, 'a [title="Edit"]').click()
        self.clear_form(contact, wd)
        self.fill_contact_form(contact, wd)
        wd.find_element(By.NAME, 'update').click()
        self.return_to_home_page()

    def delete(self):
        wd = self.app.wd
        self.return_to_home_page()
        wd.find_element(By.NAME, 'selected[]').click()
        wd.find_element(By.NAME, 'delete').click()
        self.return_to_home_page()

    def count(self):
        wd = self.app.wd
        self.return_to_home_page()
        return len(wd.find_elements(By.NAME, 'selected[]'))

    def get_contact_list(self):
        wd = self.app.wd
        self.return_to_home_page()
        contacts = []
        for elements in wd.find_elements(By.CSS_SELECTOR,'tr[name=entry]'):
            id = elements.find_element(By.CSS_SELECTOR,'tr[name=entry] td.center').get_attribute('id')
            lastname =elements.find_element(By.CSS_SELECTOR,'tr[name=entry] td:nth-child(2)')
            firstname = elements.find_element(By.CSS_SELECTOR, 'tr[name=entry] td:nth-child(3)')
            address =elements.find_element(By.CSS_SELECTOR,'tr[name=entry] td:nth-child(4)')

            contacts.append(Contact(id=id,firstname=firstname,lastname=lastname,address=address))
        return contacts


