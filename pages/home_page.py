from pages.base_page import BasePage


class HomePage(BasePage):
    def open_home_page(self):
        self.page.goto('https://magento.softwaretestingboard.com/')

    def click_men_section(self):
        self.page.locator('//nav//span[text()="Men"]').click()
