from selenium import webdriver
from selenium.webdriver.common.by import By


wd = webdriver.Firefox()
wd.implicitly_wait(30)

wd.get("https://localhost/addressbook/")
wd.find_element(By.NAME,'user').send_keys('admin')
wd.find_element(By.NAME,'pass').send_keys('secret')
wd.find_element(By.CSS_SELECTOR,'#LoginForm [type=submit]').click()
wd.find_element(By.CSS_SELECTOR,'a[href="edit.php"]').click()

wd.find_element(By.NAME, 'firstname').send_keys('Иван')
wd.find_element(By.NAME, 'middlename').send_keys('Иванов')
wd.find_element(By.NAME, 'lastname').send_keys('Иванович')
wd.find_element(By.NAME, 'address').send_keys('Москва')
wd.find_element(By.CSS_SELECTOR, '[value=Enter]').click()
wd.get("https://localhost/addressbook/")
wd.find_element(By.LINK_TEXT,'Logout').click()



# input("Тест завершен. Нажмите Enter в консоли PyCharm, чтобы закрыть браузер...")



