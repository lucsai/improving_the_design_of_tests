from .pages.basket_page import BasketPage

link = "https://selenium1py.pythonanywhere.com"

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.should_be_empty_basket()
    page.should_be_message_about_empty_basket()