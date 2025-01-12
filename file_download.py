from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

# Открываем браузер
browser = webdriver.Chrome()

try:
    # Открываем указанную страницу
    browser.get("http://suninjuly.github.io/file_input.html")
    print("Страница загружена.")
    
    # Заполняем текстовые поля: имя, фамилия, email
    browser.find_element(By.NAME, "firstname").send_keys("John")
    browser.find_element(By.NAME, "lastname").send_keys("Doe")
    browser.find_element(By.NAME, "email").send_keys("john.doe@example.com")
    print("Текстовые поля заполнены.")
    
    # Создаем временный текстовый файл
    with open("temp.txt", "w") as file:
        file.write("This is a test file.")
    file_path = os.path.abspath("temp.txt")
    
    # Загружаем файл
    file_input = browser.find_element(By.ID, "file")
    file_input.send_keys(file_path)
    print("Файл загружен.")
    
    # Нажимаем кнопку "Submit"
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()
    print("Кнопка 'Submit' нажата.")
    
    # Ждем появления алерта и выводим его текст
    alert = browser.switch_to.alert
    alert_text = alert.text
    print(f"Алерт текст: {alert_text}")
    print(alert_text.split()[-1])  # Выводим число из текста алерта

except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    # Удаляем временный файл
    if os.path.exists("temp.txt"):
        os.remove("temp.txt")
    # Закрываем браузер
    time.sleep(10)
    browser.quit()

