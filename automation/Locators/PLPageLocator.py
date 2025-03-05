class PLPageLocator:
    PRODUCT_LIST = "//ul[@id='collection']/li/following::h3/a"
    DESCRIPTION_HEADING = "//div[@class='tabs-inner']/h2"
    PRODUCT_PRICE = "//p[@class='s1pr price']"
    GEARUP_NAV = "(//li[@class='sub'])[2]"
    RUNNING_SUBNAV = "//ul[@data-type='horizontal-nav']/li/ul/li/ul/li/a[contains(.,'Running')]"
    SOR_BY_FILTER = "//span[@class='bv_mainselect']"
    SORT_ATOZ = "//a[contains(.,' Alphabetically, A-Z')]"
    SORT_RUNNING_PRODUCTS_LIST = "//a[contains(.,'Nurvv Runn Smart Insoles')]"

