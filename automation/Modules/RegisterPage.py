import time

from automation.Locators.HPageLocators import HPageLocators
from automation.Locators.RegisterPageLocator import RegPageLoc
from automation.Test_Data.testdata import TestData


class RegisterPage:
    def __init__(self, page):
        self.page = page

    def create_account(self):
        page = self.page
        page.locator(HPageLocators.LOGO_IMG).click()
        time.sleep(10)
        page.locator(RegPageLoc.SIGNIN_BTN).click()
        page.locator(RegPageLoc.CREATE_ACCOUNT_BTN).click()
        page.locator(RegPageLoc.FIRST_NAME).fill(TestData.firstname)
        page.locator(RegPageLoc.LAST_NAME).fill(TestData.lastname)
        page.locator(RegPageLoc.EMAIL_ADDRESS).fill(TestData.email)
        page.locator(RegPageLoc.NEW_PASSWORD).fill(TestData.password)
        page.locator(RegPageLoc.CREATE_ACCOUNT_SUBMIT_BTN).click()

    def login_account(self):
        page = self.page
        page.locator(RegPageLoc.SIGNIN_BTN).click()
        page.locator(RegPageLoc.LOGIN_EMAIL_ADDRESS).fill(TestData.email)
        page.locator(RegPageLoc.LOGIN_PASSWORD).fill(TestData.password)
        page.locator(RegPageLoc.LOGIN_BTN).click()
        page.locator(HPageLocators.LOGO_IMG).click()

    def invalid_account(self):
        page = self.page
        page.locator(RegPageLoc.SIGNIN_BTN).click()
        page.locator(RegPageLoc.LOGIN_EMAIL_ADDRESS).fill(TestData.invalid_email)
        page.locator(RegPageLoc.LOGIN_PASSWORD).fill(TestData.invalid_password)
