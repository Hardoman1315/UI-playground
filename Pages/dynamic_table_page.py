import allure
from selenium.webdriver.common.by import By
from Pages.base_page import BasePage


class DynamicTablePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, timeout=60)

    warning_text = (By.XPATH, '//*[@class="bg-warning"]')
    chrome_text = (By.XPATH, '//*[text()="Chrome"]/..//*[contains(text(), "%")]')

    @allure.step("Открыть целевую страницу")
    def open_target_page(self) -> None:
        self.open_page('http://uitestingplayground.com/dynamictable')

    @allure.step("Получить нагрузку Chrome на процессор")
    def get_chrome_cpu(self) -> str:
        return self.get_element_text(self.chrome_text)

    @allure.step("Получить нагрузку со строки предупреждения")
    def get_warning_cpu(self) -> str:
        text = self.get_element_text(self.warning_text)
        text = text.replace("Chrome CPU:", "").strip()
        return text

    @allure.step("Сравнить нагрузку Chrome с указанной в предупреждении")
    def check_cpu_loading(self) -> None:
        warning = self.get_warning_cpu()
        chrome = self.get_chrome_cpu()
        assert warning == chrome, (
            '[FAILED] Values are not equal'
        )
