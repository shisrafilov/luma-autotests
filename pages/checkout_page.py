from playwright.sync_api import expect

from pages.base_page import BasePage


class CheckoutPage(BasePage):
    def fill_in_shipping_data(self):
        self.page.locator('//form[@data-bind="submit:login"]//input[@id="customer-email"]').fill('test@test.te')
        self.page.locator('//input[@name="firstname"]').fill('John')
        self.page.locator('//input[@name="lastname"]').fill('Smith')
        self.page.locator('//input[@name="street[0]"]').fill('Elm Street')
        self.page.locator('//input[@name="city"]').fill('Los Angeles')
        self.page.locator('//select[@name="region_id"]').select_option(label='California')
        self.page.locator('//input[@name="postcode"]').fill('12345')
        self.page.locator('//input[@name="telephone"]').fill('+11234567890')
        self.page.locator('//input[@name="ko_unique_1"]').click()

    def click_next(self):
        self.page.locator('//button[@data-role="opc-continue"]').click()

    def place_order(self):
        self.page.locator('//button[contains(@class, "action primary checkout")]').click()

    def expect_to_see_success_message(self):
        message = self.page.locator('//div[@class="checkout-success"]')
        expect(message).to_be_visible()
