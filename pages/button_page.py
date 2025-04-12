import allure

import curl
from pages.base_page import BasePage
from locators.button_locators import ButtonPageLocators

class ButtonPage(BasePage):
    @allure.step("Кликнуть на ссылку Яндекс и дождаться загрузки сайта")
    def click_logo_yandex(self):
        self.click_on_element(ButtonPageLocators.BUTTON_HOME_PAGE_DZEN)

    @allure.step("Проверить редирект Дзен")
    def yredirect_in_dzen(self):
        actual_curl = self.redirect_dzen_url(curl.dzen_redirect_url)
        assert "https://dzen.ru/?yredirect=true" in actual_curl
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    @allure.step("Кликнуть на ссылку Самокат и дождаться загрузки сайта")
    def click_logo_scooter(self):
        self.click_on_element(ButtonPageLocators.BUTTON_HOME_PAGE_SCOOTER)

    @allure.step("Проверить перехода по ссылке Самокат")
    def open_in_main_site(self):
        actual_curl = self.open_web_page(curl.main_site)
        assert "https://qa-scooter.praktikum-services.ru/" in actual_curl

    @allure.step("Проверить перехода на окно формы Для кого самокат")
    def page_for_whom_scooter(self):
        actual_curl = self.open_web_page(curl.main_site)
        assert "https://qa-scooter.praktikum-services.ru/order" in actual_curl

    @allure.step("Кликнуть на кнопку заказать в верхней части страницы")
    def click_order_button_above(self):
        self.click_on_element(ButtonPageLocators.ORDER_BUTTON_ABOVE)

    @allure.step("Кликнуть на кнопку заказать в нижней части страницы")
    def click_order_button_below(self):
        button_locator = ButtonPageLocators.button_order_bot()
        self.scroll_to_element_with_centering(button_locator)
        self.click_on_element_with_centering(button_locator)

    @allure.step("Закрыть вкладку Куки")
    def accept_cookies(self):
        self.click_on_element(ButtonPageLocators.COOKIE_BUTTON)
