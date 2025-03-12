from automation.Modules.CartPage import CartPage
from automation.Modules.HomePage import HomePage


def test_add_to_cart_page(launch_browser):
    page = launch_browser
    cart_page = CartPage(page)
    home_page = HomePage(page)
    home_page.do_search("Smart watches")
    cart_page.add_to_cart()
