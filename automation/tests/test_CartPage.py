from automation.Modules.CartPage import CartPage
from automation.Modules.HomePage import HomePage
import json

with open("test_data.json") as file:
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
