import allure
from selene import be, by

@allure.title("Добавление товара в корзину")
def test_add_product(setup_browser):
    browser = setup_browser
    browser.driver.set_window_size(1920, 1200)

    with allure.step("Открываем главную страницу"):
        browser.open("https://www.dom-knigi.ru/")


    with allure.step("Переходим в католог Книги"):
        browser.element('.top-catalog-menu-title').click()


    with allure.step("Выбираем книги и добавляем в корзину"):
        browser.element('.embed-responsive-item').click()
        browser.element('#bx_3966226736_768460_7e1b8e3524755c391129a9d7e6f2d206_basket_actions').click()
        browser.element('span.popup-window-close-icon').click()
        browser.element('#bx_3966226736_768458_362ce596257894d11ab5c1d73d13c755_basket_actions').click()
        browser.element('//*[@id="CatalogSectionBasket_bx_3966226736_768458_362ce596257894d11ab5c1d73d13c755"]/div[3]/button[1]').click()

    with allure.step("Проверяем наличие добавленного товара в корзине"):
        browser.element(by.partial_text('В корзине 2 товара')).should(be.visible)