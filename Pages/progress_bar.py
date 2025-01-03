import re
import allure
from selenium.webdriver.common.by import By
from Pages.base_page import BasePage


class ProgressBar(BasePage):
    def __init__(self, driver):
        super().__init__(driver, timeout=60)

    start_btn = (By.XPATH, '//*[@id="startButton"]')
    stop_btn = (By.XPATH, '//*[@id="stopButton"]')
    progress_bar_counter = (By.XPATH, '//*[@id="progressBar"]')
    result = (By.XPATH, '//*[@id="result"]')


    @allure.step('Нажать кнопку "Start"')
    def click_start_btn(self) -> None:
        self.click_element(self.start_btn)

    @allure.step('Подождать достижения 75% на шкале прогресса')
    def wait_till_75(self) -> None:
        text = self.get_element_text(self.progress_bar_counter)
        while text != "75%":
            text = self.get_element_text(self.progress_bar_counter)
        self.click_stop_btn()

    @allure.step('Нажать кнопку "Stop"')
    def click_stop_btn(self) -> None:
        self.click_element(self.stop_btn)

    @allure.step("Получить значение 'Result'")
    def get_result_value(self) -> int:
        text = self.get_element_text(self.result)
        match = re.findall(r"\d", text)[0]
        return int(match)

    @allure.step('Проверить что значение "Result" меньше 5')
    def is_result_less_5(self) -> None:
        assert self.get_result_value() < 5, (
            '[Failed] result is not less than 5'
        )

    @allure.step("Получить значение 'Duration'")
    def get_duration_value(self) -> int:
        text = self.get_element_text(self.result)
        match = re.findall(r"\d", text)[1:6]
        return int(''.join(match))

    @allure.step("Проверить что значение 'Duration' меньше 17000")
    def is_duration_less_17k(self) -> None:
        assert self.get_duration_value() < 17000, (
            '[Failed] duration is not less than 17000'
        )
