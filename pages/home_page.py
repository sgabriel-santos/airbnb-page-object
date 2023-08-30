from pages.base_page import BasePage
from locators.locators import HomeLocators
from selenium.webdriver.common.keys import Keys
from time import sleep


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        driver.get('https://www.airbnb.com.br/')

    def save_cookie(self):
        self.click(HomeLocators.cookie_buttons)
        self.click(HomeLocators.button_save_cookie)
    
    def find_accommodation(self):
        self.click(HomeLocators.button_search_icon)
        self.enter_text(HomeLocators.field_local, 'Manaus AM')
        self.click(HomeLocators.button_checkin)
        self.click(HomeLocators.button_initial_date)
        self.click(HomeLocators.button_final_date)
        self.click(HomeLocators.button_guests)
        self.click(HomeLocators.button_increase_adults)
        self.click(HomeLocators.button_increase_adults)
        self.click(HomeLocators.button_search)
        self.get_elements(HomeLocators.card_content)
    
    def enable_price(self):
        self.click(HomeLocators.button_switch)
        self.get_elements(HomeLocators.card_content)

    def expand_map(self):
        self.click(HomeLocators.button_expand_map)
        return self.get_text(HomeLocators.label_show_list)
    
    def minimize_map(self):
        self.click(HomeLocators.button_minimize_map)

    def add_filter_min_max_price(self):
        self.enter_text(HomeLocators.field_price_filter_min, Keys.CONTROL + 'a')
        self.enter_text(HomeLocators.field_price_filter_min, 1000)
        self.enter_text(HomeLocators.field_price_filter_max, Keys.CONTROL + 'a')
        self.enter_text(HomeLocators.field_price_filter_max, 2000)

    def add_filter_2_room(self):
        self.click(HomeLocators.button_2_rooms)
    
    def click_btn_save_filter(self):
        self.click(HomeLocators.button_save_filters)
        sleep(2.5)
        return self.get_text(HomeLocators.label_count_filters)
    
    def apply_filter(self):
        self.click(HomeLocators.button_filter)
        return self.get_text(HomeLocators.label_filter)