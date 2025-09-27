import pandas as pd
from selenium.webdriver.common.by import By
from utils.selenium import wait_element_clickable
from utils.formatters import format_price
from utils.elements import click_element_add, click_element_save_and_quit

class NeighborhoodPage:
    def __init__(self, driver):
        self.driver = driver
        self.DESCRIPTION_INPUT = (By.ID, "descricao")
        self.SHOW_DELIVERY_SWITCH = (By.CSS_SELECTOR, "label[for='delivery']")
        self.PRICE_INPUT = (By.CSS_SELECTOR, "input[placeholder='Valor MotoBoy']")
        self.CITY_DROPDOWN = (By.CSS_SELECTOR, "#s2id_cidade_id a.select2-choice.select2-default")
        self.CITY_SEARCH_INPUT = (By.CSS_SELECTOR, "input.select2-input.select2-focused")

    def add_new_neighborhood(self, neighborhood, price, city):
        if pd.isna(neighborhood):
            return

        click_element_add(self.driver)

        self.fill_description(neighborhood)
        self.mark_show_delivery()

        if not pd.isna(price):
            self.fill_price(price)

        if not pd.isna(city):
            self.fill_city(city)

        click_element_save_and_quit(self.driver)

    def fill_description(self, neighborhood):
        element = wait_element_clickable(self.driver, *self.DESCRIPTION_INPUT)
        element.send_keys(neighborhood.upper())

    def mark_show_delivery(self):
        element = wait_element_clickable(self.driver, *self.SHOW_DELIVERY_SWITCH)
        element.click()

    def fill_price(self, price):
        element = wait_element_clickable(self.driver, *self.PRICE_INPUT)
        element.send_keys(format_price(price))

    def fill_city(self, city):
        city_state = f"{city.upper()} - RS"

        wait_element_clickable(self.driver, *self.CITY_DROPDOWN).click()
        search = wait_element_clickable(self.driver, *self.CITY_SEARCH_INPUT)
        search.send_keys(city)

        try:
            option_selector = (By.XPATH, f"//div[contains(text(), '{city_state}')]")
            option = wait_element_clickable(self.driver, *option_selector)
            option.click()
        except Exception as e:
            print(f"Erro ao selecionar a cidade '{city}': {e}")
