from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import BookPageLocators



class ProductPage(BasePage):
    def add_book_to_basket(self):
        add_to_basket = self.browser.find_element(*BookPageLocators.ADD_TO_CART_BUTTON)
        add_to_basket.click()

    def should_be_right_book_and_price(self):
        try:
            price = self.browser.find_element(*BookPageLocators.BOOK_PRICE)
            basket_price = self.browser.find_element(*BookPageLocators.BOOK_MESSAGE_PRICE)
            assert price.text == basket_price.text, "Wrong price"
        except:
            print("Wrong price!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

        try:
            name = self.browser.find_element(*BookPageLocators.BOOK_NAME)
            basket_name = self.browser.find_element(*BookPageLocators.BOOK_MESSAGE_NAME)
            assert name.text == basket_name.text, "Wrong name"
        except:
            print("Wrong name!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*BookPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_is_disappeared(self):
        assert self.is_disappeared(*BookPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared"
