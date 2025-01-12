from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Открываем браузер
browser = webdriver.Chrome()

try:
    # Открываем указанную страницу
    browser.get("https://suninjuly.github.io/selects1.html")
    
    # Находим числа на странице
    num1 = int(browser.find_element(By.ID, "num1").text)
    num2 = int(browser.find_element(By.ID, "num2").text)
    
    # Считаем сумму
    total = str(num1 + num2)
    
    # Выбираем сумму в выпадающем списке
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(total)
    
    # Нажимаем кнопку "Submit"
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    
    # Ждем появления алерта и получаем текст
    alert = browser.switch_to.alert
    alert_text = alert.text
    print(alert_text.split()[-1])  # Выводим число из текста алерта

finally:
    # Закрываем браузер
    time.sleep(10)  # Даем немного времени, чтобы визуально проверить результат
    browser.quit()


