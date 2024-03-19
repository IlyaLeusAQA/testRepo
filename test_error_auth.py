"""И домашнее задание по уровню сложности:
Уровень 1:
1. Открыть страницу https://google.com
2. Нажать кнопку "Войти"
3. Не заполнять поле email
4. Нажать кнопку "Далее"
5. Проверить наличие ошибки
Уровень 2:
1. Открыть страницу https://google.com
2. Нажать кнопку "Почта"
3. Не заполнять поле email
4. Нажать кнопку "Далее"
5. Проверить наличие ошибки
Уровень 3:
1. Открыть страницу https://google.com
2. Нажать кнопку "Картинки"
3. Проверить наличие текста "картинки" под иконкой google
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()

LOGIN_BUTTON = (By.XPATH, "//*[@aria-label='Войти']")
NEXT_BUTTON = (By.XPATH, "//*[@id='identifierNext']")
ERROR_TEXT = (By.XPATH, "//*[text()='Введите адрес электронной почты или номер телефона.']")
POSTMAIL_BUTTON = (By.XPATH, "//*[@aria-label='Почта (откроется новая вкладка)']")
ENTER_BUTTON = (By.XPATH, "//*[@data-action='sign in']")
NEXT_STEP_IN_POST_BUTTON = (By.XPATH, "//*[text()='Далее']")
CAPTURE_BUTTON = (By.XPATH, "//*[@aria-label='Поиск картинок (откроется новая вкладка)']")
TEXT_CAPTURE = (By.XPATH, "//*[text()='Картинки']")

def find_element(driver, locator, time=5):
    return WebDriverWait(driver, time).until(expected_conditions.presence_of_element_located(locator))

def test_error_auth():
    driver.get("https://google.com")
    find_element(driver, LOGIN_BUTTON).click()
    find_element(driver, NEXT_BUTTON).click()
    find_element(driver, ERROR_TEXT)

def test_error_in_postmail():
    driver.get("https://google.com")
    find_element(driver, POSTMAIL_BUTTON).click()
    find_element(driver, ENTER_BUTTON).click()
    find_element(driver, NEXT_STEP_IN_POST_BUTTON).click()
    find_element(driver, ERROR_TEXT)

def test_having_capture():
    driver.get("https://google.com")
    find_element(driver, CAPTURE_BUTTON).click()
    find_element(driver, TEXT_CAPTURE)
