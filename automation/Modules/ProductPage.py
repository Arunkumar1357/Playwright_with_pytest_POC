from automation.Locators.HPageLocators import HPageLocators
from automation.Locators.PLPageLocator import PLPageLocator


class ProductPage:
    def __init__(self, page):
        self.page = page

    def click_the_product(self, selector):
        product_element = self.page.locator(selector).first
        assert product_element.is_visible(), "Product is not visible!"
        product_name = product_element.first.text_content()
        print(f'Product name is - {product_name}')
        product_element.first.click()
        return product_name

    def get_product_description(self):
        description_element = self.page.locator(PLPageLocator.DESCRIPTION_HEADING).first
        description_element.first.is_visible(), "Description is not visible!"
        description = description_element.first.text_content()
        print(f'Product description is - {description}')
        return description

    def get_product_price(self):
        price_element = self.page.locator(PLPageLocator.PRODUCT_PRICE)
        price_element.is_visible(), "Price is not visible!"
        price = price_element.text_content()
        print(f'Product price is - {price}')
        self.page.locator(HPageLocators.LOGO_IMG).click()
        return price

    def sort_by_product(self):
        self.page.locator(PLPageLocator.GEARUP_NAV).click()
        self.page.locator(PLPageLocator.RUNNING_SUBNAV).click()
        self.page.locator(PLPageLocator.SOR_BY_FILTER).click()
        self.page.locator(PLPageLocator.SORT_ATOZ).click()
        text_visible = self.page.locator(PLPageLocator.SORT_RUNNING_PRODUCTS_LIST).text_content()
        print(f'Sort list visibility - {text_visible}')
        self.page.locator(HPageLocators.LOGO_IMG).click()

    def filter_by_brand(self):
        self.page.locator(PLPageLocator.SMARTSTYLE_NAV).click()
        self.page.locator(PLPageLocator.SMARTWATCH_SUBNAV).click()
        brand_name = self.page.locator(PLPageLocator.BRAND_CHECKBOX).text_content().strip()
        brand_name = ''.join([i for i in brand_name if not i.isdigit() and i not in "()."]).strip()
        self.page.locator(PLPageLocator.BRAND_CHECKBOX).click()
        self.page.wait_for_timeout(1000)
        filter_brand_name = self.page.locator(PLPageLocator.BRAND_LIST_TEXT).text_content().strip()
        assert brand_name == filter_brand_name, f"Brand name mismatch! Expected Brand Name: {brand_name}, Actual Brand Name: {filter_brand_name}"
        print(f'Brand name is - {brand_name}')
        print(f'Brand name filter is - {filter_brand_name}')
        self.page.locator(HPageLocators.LOGO_IMG).click()

    def sort_by_particular_price(self, min_number: float, max_number: float) -> bool:
        minimum = str(min_number)
        maximum = str(max_number)
        self.page.locator(PLPageLocator.MINIMUM_PRICE).fill(minimum)
        self.page.locator(PLPageLocator.MAXIMUM_PRICE).fill(maximum)
        self.page.wait_for_timeout(1000)
        min_product_price = self.page.locator(PLPageLocator.PRODUCT_PRICE_LIST).first.text_content().replace("₹",
                                                                                                             "").replace(
            ",", "").strip()
        max_product_price = self.page.locator(PLPageLocator.PRODUCT_PRICE_LIST).last.text_content().replace("₹",
                                                                                                            "").replace(
            ",", "").strip()
        print(f'Minimum price is - {minimum}')
        print(f'Maximum price is - {maximum}')
        print(f'Minimum price product prize is - {min_product_price}')
        print(f'Maximum price product prize is - {max_product_price}')
        min_number_actual = float(min_product_price)
        max_number_actual = float(max_product_price)

        if min_number_actual >= min_number and max_number_actual <= max_number:
            print("Product price is filtered under the given price range")
            return True
        else:
            print("Product price is not filtered correctly")
            return False

    def product_list_view(self):
        self.page.locator(PLPageLocator.GEARUP_NAV).click()
        self.page.locator(PLPageLocator.RUNNING_SUBNAV).click()
        self.page.wait_for_timeout(1000)
        self.page.locator(PLPageLocator.LIST_VIEW_BTN).click()

    def product_grid_view(self):
        self.page.locator(PLPageLocator.GEARUP_NAV).click()
        self.page.locator(PLPageLocator.RUNNING_SUBNAV).click()
        self.page.wait_for_timeout(1000)
        self.page.locator(PLPageLocator.GRID_VIEW_BTN).click()

    def remove_all_brand_filter(self):
        self.page.locator(PLPageLocator.GEARUP_NAV).click()
        self.page.locator(PLPageLocator.RUNNING_SUBNAV).click()
        self.page.locator(PLPageLocator.BRAND_CHECKBOX).click()

