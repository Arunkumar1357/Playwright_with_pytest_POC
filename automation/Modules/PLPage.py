from automation.Locators.HPageLocators import HPageLocators
from automation.Locators.PLPageLocator import PLPageLocator


class PLPage:
    def __init__(self, page):
        self.page = page

    def sort_by_product(self):
        page = self.page
        page.locator(PLPageLocator.GEARUP_NAV).click()
        page.locator(PLPageLocator.RUNNING_SUBNAV).click()
        page.locator(PLPageLocator.SOR_BY_FILTER).click()
        page.locator(PLPageLocator.SORT_ATOZ).click()
        text_visible = page.locator(PLPageLocator.SORT_RUN_PRODUCT_LIST).text_content()
        print(f'Sort list visibility - {text_visible}')
        page.locator(HPageLocators.LOGO_IMG).click()

    def filter_by_brand(self):
        page = self.page
        page.locator(PLPageLocator.SMARTSTYLE_NAV).click()
        page.locator(PLPageLocator.SMARTWATCH_SUBNAV).click()
        brand_name = page.locator(PLPageLocator.BRAND_CHECKBOX).text_content().strip()
        brand_name = ''.join([i for i in brand_name if not i.isdigit() and i not in "()."]).strip()
        page.locator(PLPageLocator.BRAND_CHECKBOX).click()
        page.wait_for_timeout(1000)
        filter_brand_name = page.locator(PLPageLocator.BRAND_LIST_TEXT).text_content().strip()
        assert brand_name == filter_brand_name, f"Brand name mismatch! Expected: {brand_name}, Actual: {filter_brand_name}"
        print(f'Brand name is - {brand_name}')
        print(f'Brand name filter is - {filter_brand_name}')
        page.locator(HPageLocators.LOGO_IMG).click()

    def sort_by_particular_price(self, min_number: float, max_number: float) -> bool:
        page = self.page
        minimum = str(min_number)
        maximum = str(max_number)
        page.locator(PLPageLocator.MINIMUM_PRICE).fill(minimum)
        page.locator(PLPageLocator.MAXIMUM_PRICE).fill(maximum)
        page.wait_for_timeout(1000)
        min_product_price = page.locator(PLPageLocator.PRODUCT_PRICE_LIST).first.text_content().replace("₹",
                                                                                                        "").replace(",",
                                                                                                                    "").strip()
        max_product_price = page.locator(PLPageLocator.PRODUCT_PRICE_LIST).last.text_content().replace("₹", "").replace(
            ",", "").strip()

        print(f'Minimum price is - {minimum}')
        print(f'Maximum price is - {maximum}')
        print(f'Minimum price product price is - {min_product_price}')
        print(f'Maximum price product price is - {max_product_price}')

        min_number_actual = float(min_product_price)
        max_number_actual = float(max_product_price)

        if min_number_actual >= min_number and max_number_actual <= max_number:
            print("Product price is filtered under the given price range")
            return True
        else:
            print("Product price is not filtered correctly")
            return False

    def product_list_view(self):
        page = self.page
        page.locator(PLPageLocator.GEARUP_NAV).click()
        page.locator(PLPageLocator.RUNNING_SUBNAV).click()
        page.wait_for_timeout(1000)
        page.locator(PLPageLocator.LIST_VIEW_BTN).click()

    def product_grid_view(self):
        page = self.page
        page.locator(PLPageLocator.GEARUP_NAV).click()
        page.locator(PLPageLocator.RUNNING_SUBNAV).click()
        page.wait_for_timeout(1000)
        page.locator(PLPageLocator.GRID_VIEW_BTN).click()

    def remove_all_brand_filter(self):
        page = self.page
        page.locator(PLPageLocator.GEARUP_NAV).click()
        page.locator(PLPageLocator.RUNNING_SUBNAV).click()
        page.locator(PLPageLocator.BRAND_CHECKBOX).click()

    def filter_instock_product(self):
        page = self.page
        page.locator(PLPageLocator.TECH_ESSENTIAL_NAV).click()
        page.locator(PLPageLocator.APPLE_WATCH_NAV).click()

    def filter_instock_products_and_verify_count_changing(self):
        page = self.page
        page.locator(PLPageLocator.TECH_ESSENTIAL_NAV).click()
        page.locator(PLPageLocator.APPLE_WATCH_NAV).click()
        page.wait_for_timeout(1000)

    def get_product_count(self):
        page = self.page
        return page.locator(PLPageLocator.TOTAL_PRODUCTS_COUNT).count()
