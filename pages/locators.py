from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REG_FORM = (By.ID, "register_form")

class BookPageLocators():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")

    BOOK_PRICE = (By.CSS_SELECTOR, ".col-sm-6.product_main p.price_color")
    BOOK_MESSAGE_PRICE = (By.CSS_SELECTOR, "div[class='alert alert-safe alert-noicon alert-info  fade in'] strong")

    BOOK_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    BOOK_MESSAGE_NAME = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")