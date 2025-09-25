from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from utils.selenium import wait_element_clickable

class System:
    def __init__(self, driver):
        self.driver = driver
        self.USER_INPUT = (By.CSS_SELECTOR, "input[placeholder='Usuário']")
        self.PASSWORD_INPUT = (By.CSS_SELECTOR, "input[placeholder='Senha']")
        self.LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    def login(self, user, password):
        element_user = wait_element_clickable(self.driver, *self.USER_INPUT)
        element_user.clear()
        element_user.send_keys(user)

        element_password = wait_element_clickable(self.driver, *self.PASSWORD_INPUT)
        element_password.clear()
        element_password.send_keys(password)

        enter_button = wait_element_clickable(self.driver, *self.LOGIN_BUTTON)
        enter_button.click()