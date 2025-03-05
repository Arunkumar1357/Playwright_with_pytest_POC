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
        return price
