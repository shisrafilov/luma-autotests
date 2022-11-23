from pages.base_page import BasePage


class JacketsPage(BasePage):
    def click_the_first_jacket(self):
        self.page.locator("//div[contains(@class, 'products-grid')]//li[1]").click()
