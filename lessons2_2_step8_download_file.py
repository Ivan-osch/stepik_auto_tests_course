from selenium import webdriver
from selenium.webdriver.common.by import By
import time

import os


current_dir = os.path.abspath(os.path.dirname(__file__)) 
file_path = os.path.join(current_dir, 'file.txt')
try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, ".form-group [name='firstname']").send_keys("Ivan")
    browser.find_element(By.CSS_SELECTOR, ".form-group [name='lastname']").send_keys("Petrov")
    browser.find_element(By.CSS_SELECTOR, ".form-group [name='email']").send_keys("vvv@mail.ru")
    browser.find_element(By.CSS_SELECTOR, "[type='file']").send_keys(file_path)
    browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
