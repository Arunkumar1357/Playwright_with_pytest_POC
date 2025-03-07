import json
import os

import pytest

from automation.Locators.PLPageLocator import PLPageLocator
from automation.Modules.HomePage import HomePage
from automation.Modules.ProductPage import ProductPage

current_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(current_dir, "test_data.json")

with open(json_path, "r") as file:
    test_data = json.load(file)


@pytest.mark.parametrize(
    "search_input, expected_url, expected_product_name",
    [(test_data["search_data"], test_data["expected_url"], test_data["expected_product_name"])])
def test_view_product_details(launch_browser, search_input, expected_url, expected_product_name,
                              ):
    page = launch_browser
    homepage = HomePage(page)
    product_page = ProductPage(page)
    actual_url = homepage.do_search(search_input)
    assert actual_url == expected_url, f"Search url Mismatch! Expected URL: {expected_url}, Actual URL: {actual_url}"

    actual_productname = product_page.click_the_product(PLPageLocator.PRODUCT_LIST)
    assert actual_productname == expected_product_name, f"Product name Mismatch! Expected Product Name: {expected_product_name}, Actual Product Name: {actual_productname}"
    actual_description = product_page.get_product_description()
    assert actual_description is not None, f"Product description is empty!"

    actual_price = product_page.get_product_price()
    assert actual_price is not None, f"Product price is empty!"


def test_sort_by_product(launch_browser):
    page = launch_browser
    product_page = ProductPage(page)
    product_page.sort_by_product()


def test_verify_brand_filter(launch_browser):
    page = launch_browser
    product_page = ProductPage(page)
    product_page.filter_by_brand()


def test_verify_filtering_particular_price_product(launch_browser):
    page = launch_browser
    homepage = HomePage(page)
    product_page = ProductPage(page)
    homepage.do_search("Smartwatch")
    price_filtered = product_page.sort_by_particular_price(2000.00, 8000.00)
    assert price_filtered, "price filter is incorrect"


def test_verify_list_view(launch_browser):
    page = launch_browser
    product_page = ProductPage(page)
    product_page.product_list_view()
    is_collection_visible = page.locator(PLPageLocator.COLLECTION_LIST).is_visible()
    assert is_collection_visible, "The product collection has not changed to the list view format"


def test_verify_grid_view(launch_browser):
    page = launch_browser
    product_page = ProductPage(page)
    product_page.product_grid_view()
    is_collection_visible = page.locator(PLPageLocator.COLLECTION_GRID).is_visible()
    assert is_collection_visible, "The product collection has not changed to the grid view format"


def test_remove_all_brand_filter(launch_browser):
    page = launch_browser
    product_page = ProductPage(page)
    product_page.remove_all_brand_filter()
    current_filter_text = page.locator(PLPageLocator.CURRENT_FILTER_TEXT)
    page.locator(PLPageLocator.REMOVE_ALL_FILTERS).click()
    assert current_filter_text.is_visible(), f'Current filter products are not removed'
