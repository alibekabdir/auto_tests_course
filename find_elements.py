from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    # Открываем браузер и переходим на страницу
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")

    # Находим все текстовые поля
    elements = browser.find_elements(By.TAG_NAME, "input")

    # Заполняем каждое поле коротким текстом
    for element in elements:
        element.send_keys("Ответ")

    # Нажимаем кнопку отправки
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Ждем, чтобы успеть скопировать код
    time.sleep(30)

finally:
    # Закрываем браузер
    browser.quit()

