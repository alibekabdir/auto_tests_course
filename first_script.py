from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Используем корректные селекторы для поиска элементов
    input1 = browser.find_element(By.TAG_NAME, "input")  # Первый input по тегу
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name")  # По имени атрибута
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "city")  # По имени класса
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")  # По ID
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")  # По CSS-селектору
    button.click()

finally:
    # Успеваем скопировать код за 30 секунд
    time.sleep(30)
    # Закрываем браузер после всех манипуляций
    browser.quit()

# Пустая строка в конце файла