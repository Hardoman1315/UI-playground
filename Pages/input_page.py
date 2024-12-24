import allure
from selenium.webdriver.common.by import By
from Pages.base_page import BasePage


class InputPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, timeout=60)

    page_link = (By.XPATH, '//*[@href="/textinput"]')
    input_field = (By.XPATH, '//*[@class="form-control"]')
    named_btn = (By.XPATH, '//*[@class="btn btn-primary"]')

    @allure.step("Нажать на ссылку 'Text Input'")
    def click_input_page(self) -> None:
        self.click_element(self.page_link)

    # @allure.step("Нажать на поле ввода")
    # def click_input_field(self):
    #     self.click_element(self.input_field)

    @allure.step("Ввести новое значение")
    def insert_new_value(self, value: str) -> None:
        self.insert_value(self.input_field, value)

    @allure.step("Нажать на кнопку "
                 "'Button That Should Change it's "
                 "Name Based on Input Value'")
    def click_named_btn(self) -> None:
        self.click_element(self.named_btn)

    @allure.step("Получить текущее название кнопки")
    def get_btn_name(self) -> str:
        return self.get_element_text(self.named_btn)