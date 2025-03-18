import os

from automation.Locators.CheckoutPage import CheckoutPageLocators
from automation.Locators.PDPageLocators import PDPageLocators
from automation.Modules.CartPage import CartPage
from automation.Modules.HomePage import HomePage
import json

current_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(current_dir, "test_data.json")

with open(json_path, "r") as file:
    test_data = json.load(file)


def test_add_to_cart_page(launch_browser):
    page = launch_browser
    cart_page = CartPage(page)
    home_page = HomePage(page)
    home_page.do_search("Smart watches")
    cart_page.add_to_cart()


def test_checkout_page(launch_browser):
    page = launch_browser
    cart_page = CartPage(page)
    home_page = HomePage(page)
    home_page.do_search("Smart watches")
    mailid = test_data["mailid"]
    fname = test_data["firstname"]
    lname = test_data["lastname"]
    companyname = test_data["company_name"]
    address = test_data["address"]
    phn_no = test_data["phone_number"]
    cart_page.checkout(mailid, fname, lname, companyname, address, phn_no)


def test_delete_product_from_minicart(launch_browser):
    page = launch_browser
    cart_page = CartPage(page)
    home_page = HomePage(page)
    home_page.do_search("Smart watches")
    cart_page.delete_product()


def test_initial_and_final_rate_difference(launch_browser):
    page = launch_browser
    time = 5
    cart_page = CartPage(page)
    cart_page.buy_now_product()
    initial_rate_count = page.locator(PDPageLocators.CURRENT_RATE).text_content().strip()
    initial_rate = cart_page.clean_and_parse_price(initial_rate_count)
    print(f"Initial Rate: {initial_rate}")

    for _int in range(time):
        page.locator(PDPageLocators.INCREASE_PRODUCT_COUNT).click()

    page.locator(PDPageLocators.BUY_NOW_BTN).click()
    final_rate_count = page.locator(CheckoutPageLocators.TOTAL_RATE).text_content().strip()
    final_rate = cart_page.clean_and_parse_price(final_rate_count)
    print(f"Final Rate: {final_rate}")
    page.wait_for_timeout(1000)
    page.locator(CheckoutPageLocators.CHECKOUT_PAGE_LOGO_DIR).click()
    assert initial_rate != final_rate, "Product rate count should be different after increasing the count"
