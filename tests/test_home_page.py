import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.home_page import HomePage


class ProcedimentoTesteLogin(unittest.TestCase):
    service = Service(ChromeDriverManager().install())

    def setUp(self):
        self.driver = webdriver.Chrome(service=self.service)
        self.home_page = HomePage(self.driver)
        self.home_page.save_cookie()
        self.home_page.find_accommodation()
    
    def test_enable_price(self):
        self.home_page.enable_price()
    
    def test_expand_map(self):
        label_show_list = self.home_page.expand_map()
        self.assertIn('Mostrar lista', label_show_list)
        self.home_page.minimize_map()

    def test_filter_dialog(self):
        label_filter = self.home_page.apply_filter()
        self.assertIn('Filtros', label_filter)
    
    def test_filter_min_max_price(self):
        self.home_page.apply_filter()
        self.home_page.add_filter_min_max_price()
        label_count_filters = self.home_page.click_btn_save_filter()
        self.assertIn('1', label_count_filters)

    def test_add_filter_2_room(self):
        self.home_page.apply_filter()
        self.home_page.add_filter_min_max_price()
        self.home_page.add_filter_2_room()
        label_count_filters = self.home_page.click_btn_save_filter()
        self.assertIn('2', label_count_filters)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
