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
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    print("Страница загружена.")
    
    # Ожидаем, пока цена не уменьшится до $100
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    print("Цена уменьшилась до $100.")
    
    # Нажимаем на кнопку "Book"
    book_button = browser.find_element(By.ID, "book")
    book_button.click()
    print("Кнопка 'Book' нажата.")
    
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
    submit_button = browser.find_element(By.ID, "solve")
    submit_button.click()
    print("Кнопка 'Submit' нажата.")

    # Ждем появления алерта
    time.sleep(1)  # Пауза, чтобы дать время для появления алерта
    alert = WebDriverWait(browser, 10).until(EC.alert_is_present())
    alert_text = alert.text
    print(f"Алерт текст: {alert_text}")
    print(alert_text.split()[-1])  # Выводим число из текста алерта
    

except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    # Закрываем браузер
    time.sleep(10)
    browser.quit()

