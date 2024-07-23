from pages.header import Header
from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage
from pages.cart_page import CartPage
from pages.side_nav import SideNav
from pages.product_page import ProductPage
from pages.circle_page import CirclePage
from pages.help_page import HelpPage
from pages.sign_in_page import SignInPage

from pages.base_page import BasePage


class Application:
    def __init__(self, driver):

        self.base_page = BasePage(driver)

        self.header = Header(driver)
        self.main_page = MainPage(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.sign_in_page = SignInPage(driver)
        self.cart_page = CartPage(driver)
        self.side_nav = SideNav(driver)
        self.product_page = ProductPage(driver)
        self.circle_page = CirclePage(driver)
        self.help_page = HelpPage(driver)
