import allure
from selene import be, by

@allure.title("Продукт не найден")
def test_product_search_not_found(setup_browser):
    browser = setup_browser
    browser.driver.set_window_size(1920, 1200)

    with allure.step("Открываем главную страницу"):
        browser.open("https://www.dom-knigi.ru/")

    with allure.step("Ищем товар"):
        browser.element('[name="q"]').send_keys('Вилка серебрянная')
        browser.element('[name="q"]').submit()

    with allure.step("Проверяем наличие товара с названием Вилка серебрянная"):
        browser.element(by.partial_text('К сожалению, на ваш поисковый запрос ничего не найдено.')).should(be.visible)

