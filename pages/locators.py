from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REG_FORM = (By.ID, "register_form")
    EMAIL_REG_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    PASS_REG_FIELD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    PASS_REG_FIELD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REG_BUTTON = (By.CSS_SELECTOR, "#register_form > button")

class BookPageLocators():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div:nth-child(1)")

    BOOK_PRICE = (By.CSS_SELECTOR, ".col-sm-6.product_main p.price_color")
    BOOK_MESSAGE_PRICE = (By.CSS_SELECTOR, "div[class='alert alert-safe alert-noicon alert-info  fade in'] strong")

    BOOK_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    BOOK_MESSAGE_NAME = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, "div[class='basket-mini pull-right hidden-xs'] a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    ITEM_IN_BASKET = (By.CSS_SELECTOR, ".basket-items")
    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, "div[class='content'] p")