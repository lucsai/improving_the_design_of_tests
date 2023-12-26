from .pages.product_page import PageObject

def test_guest_can_add_product_to_basket(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = PageObject(browser, url)
    page.open()
    page.should_be_newYear_url()
    page.button_add_to_basket_is_present()
    page.add_product_to_basket()
    page.should_be_message_product_has_been_added_to_basket()
    page.should_be_same_product_name()
    page.should_be_same_cost_of_the_basket_as_the_product_price()