import pytest
from playwright.sync_api import Page

from pages.checkout_page import CheckoutPage
from pages.home_page import HomePage
from pages.jackets_page import JacketsPage
from pages.men_section_page import MenSectionPage
from pages.product_page import ProductPage


@pytest.fixture
def home(page: Page):
    return HomePage(page)


@pytest.fixture
def men_section(page: Page):
    return MenSectionPage(page)


@pytest.fixture
def jackets(page: Page):
    return JacketsPage(page)


@pytest.fixture
def product(page: Page):
    return ProductPage(page)


@pytest.fixture
def checkout(page: Page):
    return CheckoutPage(page)
