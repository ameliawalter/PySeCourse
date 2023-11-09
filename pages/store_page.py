from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.regions.base_region import BaseRegion


# URL_TEMPLATE = "?post_type=product"

class StorePage(BasePage):
    _products_list = (By.CSS_SELECTOR, "ul[class='products columns-4']")
    _product = (By.CSS_SELECTOR, "li[class*='product type-product']")

    @property
    def loaded(self):
        return self.is_element_displayed(*self._products_list)

    @property
    def items(self):
        return [Item(self, product) for product in self.find_elements(*self._product)]


class Item(BaseRegion):
    _name = (By.CSS_SELECTOR, "h2[class*='woocommerce-loop-product']")
    _add_to_cart_button = (By.CSS_SELECTOR, "a[class='add_to_cart_button']")

    @property
    def name(self):
        return self.find_element(*self._name).text

    def click_add_to_cart_button(self):
        self.find_element(*self._add_to_cart_button).click()




