from automation.Locators.HPageLocators import HPageLocators
from automation.Locators.PLPageLocator import PLPageLocator
from automation.Modules.HomePage import HomePage
from automation.Modules.PLPage import PLPage


def test_sort_by_product(launch_browser):
    page = launch_browser
    product_page = PLPage(page)
    product_page.sort_by_product()


def test_verify_brand_filter(launch_browser):
    page = launch_browser
    product_page = PLPage(page)
    product_page.filter_by_brand()


def test_verify_filtering_particular_price_product(launch_browser):
    page = launch_browser
    homepage = HomePage(page)
    product_page = PLPage(page)
    homepage.do_search("Smartwatch")
    price_filtered = product_page.sort_by_particular_price(2000.00, 8000.00)
    assert price_filtered, "price filter is incorrect"


def test_verify_list_view(launch_browser):
    page = launch_browser
    product_page = PLPage(page)
    product_page.product_list_view()
    is_collection_visible = page.locator(PLPageLocator.COLLECTION_LIST).is_visible()
    assert is_collection_visible, "The product collection has not changed to the list view format"


def test_verify_grid_view(launch_browser):
    page = launch_browser
    product_page = PLPage(page)
    product_page.product_grid_view()
    is_collection_visible = page.locator(PLPageLocator.COLLECTION_GRID).is_visible()
    assert is_collection_visible, "The product collection has not changed to the grid view format"


def test_remove_all_brand_filter(launch_browser):
    page = launch_browser
    product_page = PLPage(page)
    product_page.remove_all_brand_filter()
    current_filter_text = page.locator(PLPageLocator.CURRENT_FILTER_TEXT)
    page.locator(PLPageLocator.REMOVE_ALL_FILTERS).click()
    assert current_filter_text.is_visible(), f'Current filter products are not removed'


def test_filter_stock_product(launch_browser):
    page = launch_browser
    product_page = PLPage(page)
    product_page.filter_instack_product()
    last_stock_product = page.locator(PLPageLocator.LAST_STOCK_PRODUCT).is_visible()
    assert last_stock_product, "The stock product is not visible"


def test_filter_stock_and_remove_product(launch_browser):
    page = launch_browser
    product_page = PLPage(page)
    product_page.filter_instock_products_and_verify_count_changing()
    page.wait_for_timeout(5000)
    initial_product_count = product_page.get_product_count()
    page.locator(PLPageLocator.INSTOCK_CHECKBOX).click()
    page.wait_for_timeout(5000)
    filter_product_count = product_page.get_product_count()
    page.locator(PLPageLocator.REMOVE_ALL_FILTERS).click()
    page.wait_for_timeout(5000)
    final_product_count = product_page.get_product_count()
    page.locator(HPageLocators.LOGO_IMG).click()
    page.wait_for_timeout(1000)
    print(f"Initial Product Count: {initial_product_count}")
    print(f"Filter Product Count: {filter_product_count}")
    print(f"Final Product Count: {final_product_count}")
    assert initial_product_count > filter_product_count, "filtered product count is not greater than initial product count"
    assert final_product_count == initial_product_count, "final product count is not equal to initial product count"
