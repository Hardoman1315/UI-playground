import allure
from selenium.webdriver.common.by import By
from Pages.base_page import BasePage


class UnbreakableSpaces(BasePage):
    def __init__(self, driver):
        super().__init__(driver, timeout=60)

    url = 'http://uitestingplayground.com/nbsp'
    nbsp_btn = (By.XPATH, f'//button[text()="My{"\u00A0"}Button"]')

    @allure.step("Открыть целевую страницу")
    def open_target_page(self) -> None:
        self.open_page(self.url)

    @allure.step("Проверить наличие кнопки с неразрывным пробелом")
    def check_nbsp_btn(self) -> None:
        self.element_is_visible(self.nbsp_btn)
