from pages.base_page import BasePage


class MainPage(BasePage):

    def open(self):
        self.open_url('https://www.target.com/')

