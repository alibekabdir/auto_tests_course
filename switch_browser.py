from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

# Функция для вычисления значения
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

# Открываем браузер
browser = webdriver.Chrome()

try:
    # Открываем указанную страницу
    browser.get("http://suninjuly.github.io/redirect_accept.html")
    print("Страница загружена.")
    
    # Нажимаем на кнопку
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    print("Кнопка нажата.")
    
    # Переключаемся на новую вкладку
    new_tab = browser.window_handles[1]
    browser.switch_to.window(new_tab)
    print("Переключились на новую вкладку.")
    
    # Считываем значение x
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    result = calc(x)
    print(f"Значение x: {x}, вычисленный результат: {result}")
    
    # Вводим ответ в текстовое поле
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(result)
    print("Ответ введен.")
    
    # Нажимаем на кнопку "Submit"
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
    # Закрываем браузер
    time.sleep(10)
    browser.quit()

