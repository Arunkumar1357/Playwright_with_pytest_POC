import json
import os
import pytest

from automation.Locators.PDPageLocators import PDPageLocators
from automation.Modules.HomePage import HomePage
from automation.Modules.PDPage import PDPage

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
    product_detail_page = PDPage(page)
    actual_url = homepage.do_search(search_input)
    assert actual_url == expected_url, f"Search url Mismatch! Expected URL: {expected_url}, Actual URL: {actual_url}"
    actual_productname = product_detail_page.click_the_product(PDPageLocators.PRODUCT_LIST)
    assert actual_productname == expected_product_name, f"Product name Mismatch! Expected Product Name: {expected_product_name}, Actual Product Name: {actual_productname}"
    actual_description = product_detail_page.get_product_description()
    assert actual_description is not None, f"Product description is empty!"

    actual_price = product_detail_page.get_product_price()
    assert actual_price is not None, f"Product price is empty!"
