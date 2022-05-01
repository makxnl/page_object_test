from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_empty_text(self):
        empty_message_on_page = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_MESSAGE)
        empty_message = "Your basket is empty. Continue shopping"
        assert empty_message_on_page.text == empty_message, "Basket not empty"

    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEM_IN_BASKET), \
            "Item in basket"
