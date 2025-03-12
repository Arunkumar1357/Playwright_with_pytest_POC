from playwright.sync_api import Page

from automation.Locators.CartPLocators import CartPLocators
from automation.Locators.CheckoutPage import CheckoutPageLocators
from automation.Locators.HPageLocators import HPageLocators
from automation.Locators.PDPageLocators import PDPageLocators
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

    def checkout(self,mailid,fname,lname,company_name,address,phno,):
        page = self.page
        page.locator(PLPageLocator.TICWATCH_PRODUCT).click()
        page.locator(CartPLocators.ADD_TO_CART_BTN).click()
        view_cart_btn = page.locator(CartPLocators.VIEW_CART_BTN)
        view_cart_btn.wait_for(state="visible")
        view_cart_btn.click()
        checkout_btn = page.locator(PDPageLocators.CHECKOUT_BTN)
        checkout_btn.wait_for(state="visible")
        checkout_btn.click()
        page.locator(CheckoutPageLocators.EMAIL_ADDRESS).fill(mailid)
        page.locator(CheckoutPageLocators.FIRST_NAME).fill(fname)
        page.locator(CheckoutPageLocators.LAST_NAME).fill(lname)
        page.locator(CheckoutPageLocators.COMPANY_NAME).fill(company_name)
        page.locator(CheckoutPageLocators.PERSONAL_ADDRESS).fill(address)
        page.locator(CheckoutPageLocators.PHONE_NUMBER).fill(phno)
        page.locator(CheckoutPageLocators.SAVE_TEXT_BOX).click()
        page.locator(CheckoutPageLocators.SHIPPING_RADIO_BTN).click()
        page.locator(CheckoutPageLocators.BILLING_BAYNOW_BTN).click()
        page.locator(CheckoutPageLocators.CHECKOUT_PAGE_LOGO).click()

