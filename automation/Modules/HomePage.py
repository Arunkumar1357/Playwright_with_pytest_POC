from automation.Locators.HPageLocators import HPageLocators
from playwright.sync_api import Page


class HomePage:

    def __init__(self, page: Page):
        self.page = page

    def verify_logo(self):
        page = self.page
        page.wait_for_timeout(1000)
        assert page.locator(HPageLocators.LOGO_IMG).is_visible(), "Logo is not visible!"

    def product_search(self):
        page = self.page
        search = page.locator(HPageLocators.SEARCH_FIELD)
        search.fill("Smart watch")
        search.press("Enter")

    def do_search(self, search_input):
        page = self.page
        page.locator(HPageLocators.SEARCH_FIELD).click()
        page.locator(HPageLocators.SEARCH_FIELD).fill(search_input)
        page.locator(HPageLocators.SEARCH_SUBMIT).click()
        page.wait_for_timeout(1000)
        return page.url

