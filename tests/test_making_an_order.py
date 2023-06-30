import allure
from selene import be, by

@allure.title("Оформление заказа")
def test_making_an_order(setup_browser):
    browser = setup_browser
    browser.driver.set_window_size(1920, 1200)

    with allure.step("Открываем главную страницу"):
        browser.open("https://www.dom-knigi.ru/")

    with allure.step("Переходим в католог Книги"):
        browser.element('a[href="/catalog/"]').click()
        browser.element('#bx_1847241719_8226').click()

    with allure.step("Выбираем книгу и добавляем в корзину"):
        browser.element('#bx_3966226736_768457_c80764dfaf26ca80162484593ec7c29b_buy_link').click()
        browser.element('.popup-window-buttons button').click()

    with allure.step("Оформляем заказ"):
        browser.element('[data-entity="basket-checkout-button"]').click()
        browser.element('button.pull-right.btn-primary').click()
        browser.element('button.pull-right.btn-primary').click()
        browser.element('input#soa-property-2').type('PevRot@mail.ru')
        browser.element('button.pull-right.btn-primary').click()
        browser.element('#bx-soa-orderSave  a').click()

    with allure.step("Проверяем сообщение  Согласие на обработку персональных данных и отказываемся"):
        browser.element(by.partial_text('Согласие на обработку персональных данных')).should(be.visible)
        browser.element('span.main-user-consent-request-popup-button-rej').click()