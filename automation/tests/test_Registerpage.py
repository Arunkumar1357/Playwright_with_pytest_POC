from automation.Modules.RegisterPage import RegisterPage
from automation.tests.conftest import launch_browser


def test_login_account(launch_browser):
    register_page = RegisterPage(launch_browser)
    register_page.login_account()


def test_create_account(launch_browser):
    register_page = RegisterPage(launch_browser)
    register_page.create_account()

def test_create_invalid_account(launch_browser):
    register_page = RegisterPage(launch_browser)
    register_page.invalid_account()