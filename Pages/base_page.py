from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver, timeout = 60):
        self.driver = driver
        self.timeout = int(timeout)
        self.wait = WebDriverWait(driver, timeout)
        self.page_url = ''


    def element_is_visible(self, locator: WebElement or tuple[str, str]) -> WebElement:
        return WebDriverWait(self.driver, 60).until(
            ec.presence_of_element_located(locator)
        )

    def get_element_text(self, locator: WebElement or tuple[str, str]) -> str:
        return self.element_is_visible(locator).text

    def click_element(self, locator: WebElement or tuple[str, str]) -> None:
        return self.element_is_visible(locator).click()

    def insert_value(self, locator: WebElement or tuple[str, str], value: str) -> None:
        self.element_is_visible(locator).send_keys(value)

    def element_is_displayed(self, locator: WebElement or tuple[str, str]) -> None:
        is_displayed = self.element_is_visible(locator).is_displayed()
        assert is_displayed, (
            '[FAILED] requested element is not displayed'
        )

    def open_page(self, url: str) -> None:
        self.driver.get(url)
