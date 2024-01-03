from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def register_new_user(self, email, password):
        input_email = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        input_email.send_keys(email)
        input_password1 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD1)
        input_password1.send_keys(password)
        input_password2 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD2)
        input_password2.send_keys(password)
        press_register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        press_register_button.click()

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_USERNAME), "Login username is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), "Login password is not presented"

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
            assert "login" in self.url, f"expected '{'login'}' to be substring of '{self.url}'"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL), "Registration email is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD1), "Registration password1 is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD2), "Registration password2 is not presented"
