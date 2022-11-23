from playwright.sync_api import Page, expect


def test_buy_a_jacket(page: Page):
    # open a website
    page.goto('https://magento.softwaretestingboard.com/')
    # click "Men" section
    page.locator('//nav//span[text()="Men"]').click()
    # click "Jackets"
    page.locator('//a[text()="Jackets"]').click()
    # click the first jacket
    page.locator("//div[contains(@class, 'products-grid')]//li[1]").click()
    # choose size and color
    page.locator('//div[@option-label="L"]').click()
    page.locator('//div[@option-label="Blue"]').click()
    # Add To Cart
    page.locator('//button[@id="product-addtocart-button"]').click()
    # wait for success message
    message = page.locator('//div[@class="message-success success message"]')
    expect(message).to_be_visible()
    # go to cart
    page.locator('//div[@data-block="minicart"]').click()
    page.locator('//button[@id="top-cart-btn-checkout"]').click()

    # fill in shipping data
    page.locator('//form[@data-bind="submit:login"]//input[@id="customer-email"]').fill('test@test.te')
    page.locator('//input[@name="firstname"]').fill('John')
    page.locator('//input[@name="lastname"]').fill('Smith')
    page.locator('//input[@name="street[0]"]').fill('Elm Street')
    page.locator('//input[@name="city"]').fill('Los Angeles')
    page.locator('//select[@name="region_id"]').select_option(label='California')
    page.locator('//input[@name="postcode"]').fill('12345')
    page.locator('//input[@name="telephone"]').fill('+11234567890')
    page.locator('//input[@name="ko_unique_1"]').click()
    page.locator('//button[@data-role="opc-continue"]').click()

    # place order
    page.locator('//button[contains(@class, "action primary checkout")]').click()

    # expect to see success message
    message = page.locator('//div[@class="checkout-success"]')
    expect(message).to_be_visible()
