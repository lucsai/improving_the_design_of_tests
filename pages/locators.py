from selenium.webdriver.common.by import By

class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > h1")
    PRODUCT_NAME_IN_MESSAGE_1 = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    PRODUCT_PRICE_IN_MESSAGE_2 = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")