import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Функция для вычисления значения
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    # Открываем страницу
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Находим элемент-картинку и извлекаем значение атрибута valuex
    treasure = browser.find_element(By.ID, "treasure")
    x_value = treasure.get_attribute("valuex")
    y = calc(x_value)

    # Вводим ответ в текстовое поле
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(y)

    # Отмечаем checkbox "I'm the robot"
    robot_checkbox = browser.find_element(By.ID, "robotCheckbox")
    robot_checkbox.click()

    # Выбираем radiobutton "Robots rule!"
    robots_rule_radiobutton = browser.find_element(By.ID, "robotsRule")
    robots_rule_radiobutton.click()

    # Нажимаем кнопку Submit
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

    # Ожидание, чтобы увидеть результат
    time.sleep(10)

finally:
    # Закрываем браузер
    browser.quit()
