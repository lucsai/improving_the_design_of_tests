from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math

class PageObject(BasePage):
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_be_newYear_url(self):
        assert '?promo=newYear' in self.browser.current_url, 'newYear missing in url'

    def button_add_to_basket_is_present(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET), "Button 'Add to basket' is not presented"

    def add_product_to_basket(self):
        add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket.click()

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def test_message_disappeared_after_adding_product_to_basket(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not disappeared"

    def should_be_message_product_has_been_added_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE_1), 'Message about adding is not presented'

    def should_be_same_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        product_name_in_message_1 = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE_1)
        assert product_name.text == product_name_in_message_1.text, "The name of the product in the message doesn't match the name product that you actually added"

    def should_be_same_cost_of_the_basket_as_the_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        product_price_in_message_2 = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_MESSAGE_2)
        assert product_price.text == product_price_in_message_2.text, "The name of the product in the message doesn't match the name product that you actually added"