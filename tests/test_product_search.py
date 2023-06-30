import allure
from selene import be, by


@allure.title("Поиск книги по автору")
def test_product_search(setup_browser):
    browser = setup_browser
    browser.driver.set_window_size(1920, 1200)

    with allure.step("Открываем главную страницу"):
        browser.open("https://www.dom-knigi.ru/")

    with allure.step("Ищем книгу по автору "):
        browser.element('[name="q"]').send_keys('Лем С.')
        browser.element('[name="q"]').submit()

    with allure.step("Проверяем нличие книги автор которой Лен С."):
        browser.element(by.partial_text('Лем С.')).should (be.visible)