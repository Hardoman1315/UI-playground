import allure
from Pages.progress_bar import ProgressBar
from Pages.delays_page import DelaysPage
from Pages.input_page import InputPage
from Pages.dynamic_table_page import DynamicTablePage
from Pages.unbreakable_spaces_page import UnbreakableSpaces


@allure.title('Проверить работоспособность шкалы прогресса')
def test_progress_bar(driver):
    progress = ProgressBar(driver)

    progress.click_progress_page()
    progress.click_start_btn()
    progress.wait_till_75()
    progress.is_result_less_5()
    progress.save_results()
    progress.is_duration_less_21k()


@allure.title('Проверить работу теста с учётом задержек')
def test_delays(driver):
    delay = DelaysPage(driver)

    delay.click_delay_page()
    delay.check_delayed_btn()


@allure.title('Проверить автоматический ввод текста')
def test_input_text(driver):
    input_page = InputPage(driver)

    input_page.click_input_page()
    old_name = input_page.get_btn_name()
    input_page.insert_new_value('New button name')
    input_page.click_named_btn()
    new_name = input_page.get_btn_name()
    assert old_name != new_name, (
        '[FAILED] Button name stays the same'
    )


@allure.title('Проверить работу с динамически генерируемыми таблицами')
def test_dynamic_tables(driver):
    tables = DynamicTablePage(driver)

    tables.click_dynamic_table_page()
    tables.check_cpu_loading()

@allure.title("Проверить поиск с неразрывными пробелами")
def test_unbreakable_spaces(driver):
    spaces = UnbreakableSpaces(driver)

    spaces.click_spaces()
    spaces.check_nbsp_btn()
