from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

# Ссылка на начальную страницу
start_link = "http://suninjuly.github.io/find_link_text"

# Вычисление текста для поиска ссылки
encoded_text = str(math.ceil(math.pow(math.pi, math.e) * 10000))

try:
    # Инициализация браузера
    browser = webdriver.Chrome()
    browser.get(start_link)

    # Поиск зашифрованной ссылки
    link = browser.find_element(By.LINK_TEXT, encoded_text)
    link.click()

    # Заполнение формы
    browser.find_element(By.NAME, "first_name").send_keys("Ivan")
    browser.find_element(By.NAME, "last_name").send_keys("Petrov")
    browser.find_element(By.CLASS_NAME, "form-control.city").send_keys("Smolensk")
    browser.find_element(By.ID, "country").send_keys("Russia")

    # Отправка формы
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Ожидание для копирования кода
    time.sleep(10)

finally:
    # Закрытие браузера
    browser.quit()

