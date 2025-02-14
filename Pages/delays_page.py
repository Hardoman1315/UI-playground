import allure
from selenium.webdriver.common.by import By
from Pages.base_page import BasePage


class DelaysPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, timeout=60)

    url = 'http://uitestingplayground.com'
    page_link = (By.XPATH, '//*[@href="/loaddelay"]')
    delayed_button = (By.XPATH, '//*[@class="btn btn-primary"]')

    @allure.step("Открыть целевую страницу")
    def open_target_page(self) -> None:
        self.open_page(self.url)

    @allure.step("Нажать на ссылку 'Load Delay'")
    def click_delay_page(self) -> None:
        self.click_element(self.page_link)

    @allure.step("Проверить отображение кнопки 'Button Appearing After Delay'")
    def check_delayed_btn(self) -> None:
        self.element_is_displayed(self.delayed_button)
