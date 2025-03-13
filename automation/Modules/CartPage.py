from playwright.sync_api import Page
import re
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

    def checkout(self, mailid, fname, lname, company_name, address, phno, ):
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
        page.wait_for_timeout(1000)
        page.locator(CheckoutPageLocators.CHECKOUT_PAGE_LOGO).click()

    def delete_product(self):
        page = self.page
        page.locator(PLPageLocator.PRO10_PRODUCT).click()
        page.locator(CartPLocators.ADD_TO_CART_BTN).click()
        page.locator(CartPLocators.MINI_CART_REMOVE_BTN).click()
        page.wait_for_timeout(1000)
        page.locator(CartPLocators.MINI_CART_CLOSE_BTN).click()
        page.locator(HPageLocators.LOGO_IMG).click()

    def clean_and_parse_price(self, price_text: str) -> float:
        cleaned_price = re.sub(r"[^\d.]", "", price_text)
        return float(cleaned_price)

    def buy_now_product(self):
        page = self.page
        page.wait_for_timeout(1000)
        page.locator(HPageLocators.AIPOWER_PRODUCT).click()
        page.wait_for_timeout(1000)
        page.locator(PDPageLocators.COLOR_DROPDOWN).click()
        page.locator(PDPageLocators.COLOR_CHOOSING).click()
        page.locator(PDPageLocators.SIZE_DROPDOWN_BTN).click()
        page.locator(PDPageLocators.SIZE_CHOOSING).click()
        page.wait_for_timeout(1000)
