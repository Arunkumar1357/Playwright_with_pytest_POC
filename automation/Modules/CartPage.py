from playwright.sync_api import Page

from automation.Locators.CartPLocators import CartPLocators
from automation.Locators.HPageLocators import HPageLocators
from automation.Locators.PLPageLocator import PLPageLocator


class CartPage:

    def __init__(self, page: Page):
        self.page = page

    def add_to_cart(self):
        page = self.page
        product = page.locator(PLPageLocator.SMART_WATCH)
        product.wait_for(state="visible")
        product.click()
        add_to_cart_btn = page.locator(CartPLocators.ADD_TO_CART_BTN)
        add_to_cart_btn.wait_for(state="visible")
        add_to_cart_btn.click()
        page.wait_for_timeout(1000)
        view_cart_btn = page.locator(CartPLocators.VIEW_CART_BTN)
        view_cart_btn.wait_for(state="visible")

        if view_cart_btn.is_visible():
            print("View Cart Button is visible")
        else:
            print("View Cart Button is not visible")
        page.locator(CartPLocators.CLOSE_BTN).click()
        page.locator(HPageLocators.LOGO_IMG).click()
        page.wait_for_timeout(1000)
