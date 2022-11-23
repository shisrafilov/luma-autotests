from playwright.sync_api import expect

from pages.base_page import BasePage


class ProductPage(BasePage):
    def choose_size(self):
        self.page.locator('//div[@option-label="L"]').click()

    def choose_color(self):
        self.page.locator('//div[@option-label="Blue"]').click()

    def add_to_cart(self):
        self.page.locator('//button[@id="product-addtocart-button"]').click()

    def wait_for_success_message(self):
        message = self.page.locator('//div[@class="message-success success message"]')
        expect(message).to_be_visible()

    def proceed_to_checkout(self):
        self.page.locator('//div[@data-block="minicart"]').click()
        self.page.locator('//button[@id="top-cart-btn-checkout"]').click()
