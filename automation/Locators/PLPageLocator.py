class PLPageLocator:
    PRODUCT_LIST = "//ul[@id='collection']/li/following::h3/a"
    DESCRIPTION_HEADING = "//div[@class='tabs-inner']/h2"
    PRODUCT_PRICE = "//p[@class='s1pr price']"
    GEARUP_NAV = "(//li[@class='sub'])[2]"
    SMARTSTYLE_NAV = "//ul[@data-type='horizontal-nav']/li/a[contains(.,'Smart Style')]"
    RUNNING_SUBNAV = "//ul[@data-type='horizontal-nav']/li/ul/li/ul/li/a[contains(.,'Running')]"
    SMARTWATCH_SUBNAV = "(//a[contains(.,'Smart Watches')])[1]"
    SOR_BY_FILTER = "//span[@class='bv_mainselect']"
    SORT_ATOZ = "//a[contains(.,' Alphabetically, A-Z')]"
    SORT_RUNNING_PRODUCTS_LIST = "//a[contains(.,'Nurvv Runn Smart Insoles')]"
    BRAND_CHECKBOX = "(//ul[@class='check']/li)[2]"
    BRAND_LIST_TEXT = "(//span[@class='small'])[1]"

