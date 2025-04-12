import allure
import pytest

import data
from pages.order_page import OrderPage

class TestOrderScooter:
    @allure.title("Проверка заказа самоката по кнопке в верхней части страницы, 1-й набор данных")
    def test_order_scooter_top_button_successful(self, firefox_driver):
        order_page = OrderPage(firefox_driver)
        test_data = data.Credentials.order_data[0]
        order_page.click_order_button_above()
        # Заполняем форму заказа Для кого самокат
        order_page.fill_order_form_with_test_data(test_data["personal"])
        # Заполняем форму заказа Про аренду
        order_page.fill_rental_form(test_data["rental"])
        order_page.confirm_order()
        assert order_page.verify_success_message() #Проверка высплывающего окна об успешном заказе

    @allure.title("Проверка заказа самоката по кнопке в нижней части страницы, 2-й набор данных")
    def test_order_scooter_bot_button_successful(self, firefox_driver):
        order_page = OrderPage(firefox_driver)
        test_data = data.Credentials.order_data[1]
        order_page.accept_cookies()
        order_page.click_order_button_below()
        # Заполняем форму заказа Для кого самокат
        order_page.fill_order_form_with_test_data(test_data["personal"])
        # Заполняем форму заказа Про аренду
        order_page.fill_rental_form(test_data["rental"])
        order_page.confirm_order()
        assert order_page.verify_success_message()

