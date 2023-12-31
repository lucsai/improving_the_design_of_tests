from .pages.product_page import PageObject
import pytest

# @pytest.mark.parametrize('link', [0, 1, 2, 3, 4, 5, 6,
#                                   pytest.param(7, marks=pytest.mark.xfail),
#                                   8, 9])
#
# def test_guest_can_add_product_to_basket(browser, link):
#     link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
#     page = PageObject(browser, link)
#     page.open()
#     #page.should_be_newYear_url()
#     page.button_add_to_basket_is_present()
#     page.add_product_to_basket()
#     page.solve_quiz_and_get_code()
#     page.should_be_message_product_has_been_added_to_basket()
#     page.should_be_same_product_name()
#     page.should_be_same_cost_of_the_basket_as_the_product_price()

#link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
link2 = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"

# @pytest.mark.xfail
# def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
#     page = PageObject(browser, link)
#     page.open()
#     page.add_product_to_basket()
#     page.solve_quiz_and_get_code()
#     page.should_not_be_success_message()
#
# @pytest.mark.xfail
# def test_guest_cant_see_success_message(browser):
#     page = PageObject(browser, link)
#     page.open()
#     page.should_not_be_success_message()
#
# @pytest.mark.xfail
# def test_message_disappeared_after_adding_product_to_basket(browser):
#     page = PageObject(browser, link)
#     page.open()
#     page.add_product_to_basket()
#     page.solve_quiz_and_get_code()
#     page.test_message_disappeared_after_adding_product_to_basket()

def test_guest_should_see_login_link_on_product_page(browser):
    page = PageObject(browser, link2)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    page = PageObject(browser, link2)
    page.open()
    page.go_to_login_page()
