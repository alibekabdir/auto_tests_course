from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Используем правильные XPath селекторы для поиска элементов
    input1 = browser.find_element(By.XPATH, "//input[@name='first_name']")  # По атрибуту name
    input1.send_keys("Ivan")
    
    input2 = browser.find_element(By.XPATH, "//input[@name='last_name']")  # По атрибуту name
    input2.send_keys("Petrov")
    
    input3 = browser.find_element(By.XPATH, "//input[@class='form-control city']")  # По атрибуту class
    input3.send_keys("Smolensk")
    
    input4 = browser.find_element(By.XPATH, "//input[@id='country']")  # По атрибуту id
    input4.send_keys("Russia")
    
    button = browser.find_element(By.XPATH, "//button[contains(., 'Submit')]")  # По тексту кнопки
    button.click()

finally:
    # Успеваем скопировать код за 30 секунд
    time.sleep(30)
    # Закрываем браузер после всех манипуляций
    browser.quit()

# Пустая строка в конце файла
