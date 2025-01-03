import allure
from Pages.progress_bar import ProgressBar
from Pages.delays_page import DelaysPage
from Pages.input_page import InputPage
from Pages.dynamic_table_page import DynamicTablePage
from Pages.unbreakable_spaces_page import UnbreakableSpaces


@allure.suite('Набор тестов')
class Tests:
    @allure.title('Проверить работоспособность шкалы прогресса')
    def test_progress_bar(self, driver):
        driver.get('http://uitestingplayground.com/progressbar')
        progress = ProgressBar(driver)

        progress.click_start_btn()
        progress.wait_till_75()
        progress.is_result_less_5()
        progress.is_duration_less_17k()

    @allure.title('Проверить работу теста с учётом задержек')
    def test_delays(self, driver):
        driver.get('http://uitestingplayground.com')
        delay = DelaysPage(driver)

        delay.click_delay_page()
        delay.check_delayed_btn()

    @allure.title('Проверить автоматический ввод текста')
    def test_input_text(self, driver):
        driver.get('http://uitestingplayground.com/textinput')
        input_page = InputPage(driver)

        old_name = input_page.get_btn_name()
        input_page.insert_new_value('New button name')
        input_page.click_named_btn()
        new_name = input_page.get_btn_name()
        assert old_name != new_name, (
            '[FAILED] Button name stays the same'
        )

    @allure.title('Проверить работу с динамически генерируемыми таблицами')
    def test_dynamic_tables(self, driver):
        driver.get('http://uitestingplayground.com/dynamictable')
        tables = DynamicTablePage(driver)

        tables.check_cpu_loading()

    @allure.title("Проверить поиск с неразрывными пробелами")
    def test_unbreakable_spaces(self, driver):
        driver.get('http://uitestingplayground.com/nbsp')
        spaces = UnbreakableSpaces(driver)

        spaces.check_nbsp_btn()
