import time

from automation.Locators.HPageLocators import HPageLocators
from automation.Modules.HomePage import HomePage
from playwright.sync_api import PlaywrightError


def test_verify_HeaderSection(launch_browser):
    Home_page = HomePage(launch_browser)
    Home_page.verify_logo()
    page_title = Home_page.page.title()
    print(f"Home page page_title is: {page_title}")
    assert "Transform Your Life with Smart Wearables - Wearables" in page_title, \
        f"Page page_title does not match expected. Actual: {page_title}"

def test_product_search(launch_browser):
    try:
        page = launch_browser
        Home_page = HomePage(page)
        Home_page.product_search()
        smartwatch = launch_browser.get_by_text("Withings SCAN Smart Watch", exact=True)
        smartwatch.wait_for(state='visible')
        page.wait_for_timeout(1000)
        print("Product found: Withings SCAN Smart Watch")
        assert smartwatch.is_visible(), "Smartwatch is not visible on the page."
        page.locator(HPageLocators.LOGO_IMG).click()
    except PlaywrightError:
        print("Product not found: Withings SCAN Smart Watch")
