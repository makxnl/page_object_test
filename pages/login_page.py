from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.url, "This is not login page"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_FORM), "Form is not presented"

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.EMAIL_REG_FIELD)
        email_field.send_keys(email)
        pass_field1 = self.browser.find_element(*LoginPageLocators.PASS_REG_FIELD1)
        pass_field1.send_keys(password)
        pass_field2 = self.browser.find_element(*LoginPageLocators.PASS_REG_FIELD2)
        pass_field2.send_keys(password)
        reg_btn = self.browser.find_element(*LoginPageLocators.REG_BUTTON)
        reg_btn.click()