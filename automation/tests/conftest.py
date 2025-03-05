import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session",params=["chromium"])
def launch_browser(request):
    with sync_playwright() as p:
        if request.param == "chromium":
            browser = p.chromium.launch(headless=False)
        elif request.param == "firefox":
            browser = p.firefox.launch(headless=False)
        elif request.param == "webkit":
            browser = p.webkit.launch(headless=False)
        else:
            raise ValueError("Unsupported browser")
        page = browser.new_page()
        page.goto("https://wearables.in/")
        page.set_viewport_size({"width": 1350, "height": 1750})
        page.wait_for_timeout(3000)
        yield page  # Yield the Playwright page instance to tests
        browser.close()
