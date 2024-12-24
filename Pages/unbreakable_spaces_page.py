import allure
from selenium.webdriver.common.by import By
from Pages.base_page import BasePage


class UnbreakableSpaces(BasePage):
    def __init__(self, driver):
        super().__init__(driver, timeout=60)

    page_link = (By.XPATH, '//*[@href="/nbsp"]')
    nbsp_btn = (By.XPATH, '//button[text()="My Button"]')

    @allure.step("Нажать на кнопку 'Non-Breaking Space'")
    def click_spaces(self) -> None:
        self.click_element(self.page_link)

    @allure.step("Проверить наличие кнопки с неразрывным пробелом")
    def check_nbsp_btn(self) -> None:
        # Я использовал сочетание alt + 0160 для создания неразрывного пробела
        # Не уверен насколько это правильно, но XPATH его видит
        self.element_is_visible(self.nbsp_btn)
