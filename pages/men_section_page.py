from pages.base_page import BasePage


class MenSectionPage(BasePage):
    def click_jackets_category(self):
        self.page.locator('//a[text()="Jackets"]').click()
