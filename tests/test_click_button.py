import allure
import pytest

from pages.button_page import ButtonPage

class TestButton:
    @allure.title("Проверка успешного редиректа на дзен по ссылке Яндекс")
    def test_click_yandex(self, firefox_driver):
        button_page = ButtonPage(firefox_driver)
        button_page.click_logo_yandex()
        button_page.yredirect_in_dzen()

    @allure.title("Проверка успешного перехода по ссылке Самокат")
    def test_click_scooter(self, firefox_driver):
        button_page = ButtonPage(firefox_driver)
        button_page.click_order_button_above()
        button_page.click_logo_scooter()
        button_page.open_in_main_site()

    @allure.title("Проверка успешного перехода по верхней кнопке Заказать")
    def test_click_order_top(self, firefox_driver):
        button_page = ButtonPage(firefox_driver)
        button_page.click_order_button_above()
        button_page.page_for_whom_scooter()

    @allure.title("Проверка успешного перехода по верхней кнопке Заказать")
    def test_click_order_bot(self, firefox_driver):
        button_page = ButtonPage(firefox_driver)
        button_page.accept_cookies()
        button_page.click_order_button_below()
        button_page.page_for_whom_scooter()
