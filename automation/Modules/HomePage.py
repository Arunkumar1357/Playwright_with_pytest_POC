from automation.Locators.HPageLocators import HPageLocators
from playwright.sync_api import Page


class HomePage:

    def __init__(self, page: Page):
        self.page = page

    def verify_logo(self):
        assert self.page.locator(HPageLocators.LOGO_IMG).is_visible(), "Logo is not visible!"

    def product_search(self):
        search = self.page.locator(HPageLocators.SEARCH_FIELD)
        search.fill("Smart watch")
        search.press("Enter")

    def do_search(self, search_input):
        self.page.locator(HPageLocators.SEARCH_FIELD).click()
        self.page.locator(HPageLocators.SEARCH_FIELD).fill(search_input)
        self.page.locator(HPageLocators.SEARCH_SUBMIT).click()
        self.page.wait_for_timeout(1000)
        return self.page.url

