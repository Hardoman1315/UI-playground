import allure
from selenium.webdriver.common.by import By
from Pages.base_page import BasePage


class DynamicTablePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, timeout=60)

    page_link = (By.XPATH, '//*[@href="/dynamictable"]')
    warning_text = (By.XPATH, '//*[@class="bg-warning"]')
    chrome_text = (By.XPATH, '//*[text()="Chrome"]/..//*[contains(text(), "%")]')

    @allure.step("Нажать на ссылку 'Dynamic Table'")
    def click_dynamic_table_page(self) -> None:
        self.click_element(self.page_link)

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