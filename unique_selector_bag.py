from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    # Открываем сайт
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Заполняем обязательные поля
    first_name = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
    first_name.send_keys("Ivan")

    last_name = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
    last_name.send_keys("Petrov")

    email = browser.find_element(By.CSS_SELECTOR, ".first_block .third")
    email.send_keys("ivan.petrov@example.com")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    time.sleep(1)

    # Находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    # Проверяем текст успешной регистрации
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # Ожидание, чтобы увидеть результат
    time.sleep(10)
    # Закрытие браузера
    browser.quit()

