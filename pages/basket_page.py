from .base_page import BasePage
from .locators import BasePageLocators
class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasePageLocators.NOT_EMPTY_BASKET), 'The basket is not empty'
    def should_be_message_about_empty_basket(self):
        assert self.is_element_present(*BasePageLocators.MESSAGE_ABOUT_EMPTY_BASKET), "There is not a message about empty basket"