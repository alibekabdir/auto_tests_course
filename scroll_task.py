from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

# Функция для вычисления значения
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

# Открываем браузер
browser = webdriver.Chrome()

try:
    # Открываем указанную страницу
    browser.get("https://suninjuly.github.io/execute_script.html")
    print("Страница загружена.")
    
    # Считываем значение переменной x
    x_element = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.ID, "input_value"))
    )
    x = x_element.text
    result = calc(x)
    print(f"Значение x: {x}, вычисленный результат: {result}")
    
    # Прокручиваем страницу вниз
    answer_input = browser.find_element(By.ID, "answer")
    browser.execute_script("arguments[0].scrollIntoView(true);", answer_input)
    print("Поле для ответа прокручено в видимую область.")
    
    # Вводим ответ в текстовое поле
    answer_input.send_keys(result)
    print("Ответ введен.")
    
    # Выбираем checkbox "I'm the robot"
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    browser.execute_script("arguments[0].scrollIntoView(true);", checkbox)
    checkbox.click()
    print("Чекбокс отмечен.")
    
    # Переключаем radiobutton "Robots rule!"
    radiobutton = browser.find_element(By.ID, "robotsRule")
    browser.execute_script("arguments[0].scrollIntoView(true);", radiobutton)
    radiobutton.click()
    print("Радиокнопка переключена.")
    
    # Прокручиваем страницу к кнопке Submit
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    browser.execute_script("arguments[0].scrollIntoView(true);", submit_button)
    print("Кнопка 'Submit' прокручена в видимую область.")
    
    # Убедимся, что кнопка доступна для клика
    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn"))
    )
    submit_button.click()
    print("Кнопка 'Submit' нажата.")
    
    # Ждем появления алерта
    WebDriverWait(browser, 5).until(EC.alert_is_present())
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

