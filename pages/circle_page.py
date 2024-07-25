from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CirclePage(BasePage):
    BENEFIT_CELLS = (By.CSS_SELECTOR, "[data-test='@web/slingshot-components/CellsComponent/Link']")

    def verify_benefit_cells(self, number):
        links = self.find_elements(*self.BENEFIT_CELLS)

        assert len(links) == int(number), f"Expected {number} benefit cells but got {len(links)}"
        print('Test case Passed.')
