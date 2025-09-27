from selenium.webdriver.common.by import By
from utils.selenium import wait_element_clickable

class MainMenu:
    def __init__(self, driver):
        self.driver = driver
        self.MENU_ICON = (By.CSS_SELECTOR, ".fa.fa-lg.fa-fw.fa-gears")
        self.NEIGHBORHOOD_LINK = (By.CSS_SELECTOR, "a[href='#/cliente/bairro']")

    def go_to_neighborhood_page(self):
        wait_element_clickable(self.driver, *self.MENU_ICON).click()
        wait_element_clickable(self.driver, *self.NEIGHBORHOOD_LINK).click()
