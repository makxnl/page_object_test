from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import BookPageLocators


class BookPage(BasePage):
    def add_book_to_basket(self):
        add_to_basket = self.browser.find_element(*BookPageLocators.ADD_TO_CART_BUTTON)
        add_to_basket.click()

    def should_be_right_price(self):
        price = self.browser.find_element(*BookPageLocators.BOOK_PRICE)
        basket_price = self.browser.find_element(*BookPageLocators.BOOK_MESSAGE_PRICE)
        assert price.text == basket_price.text, "Wrong price"

    def should_be_right_book(self):
        name = self.browser.find_element(*BookPageLocators.BOOK_NAME)
        basket_name = self.browser.find_element(*BookPageLocators.BOOK_MESSAGE_NAME)
        assert name.text == basket_name.text, "Wrong name"
