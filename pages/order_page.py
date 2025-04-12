import allure

from pages.base_page import BasePage
from locators.order_locators import OrderPageLocators
from locators.button_locators import ButtonPageLocators

class OrderPage(BasePage):
    @allure.step("Кликнуть на кнопку заказать в верхней части страницы")
    def click_order_button_above(self):
        self.click_on_element(ButtonPageLocators.ORDER_BUTTON_ABOVE)

    @allure.step("Кликнуть на кнопку заказать в нижней части страницы")
    def click_order_button_below(self):
        button_locator = ButtonPageLocators.button_order_bot()
        self.scroll_to_element_with_centering(button_locator)
        self.click_on_element_with_centering(button_locator)


    @allure.step("Заполнить основную форму заказа Для кого самокат")
    def fill_order_form_with_test_data(self, test_data):
        self.input_text(OrderPageLocators.NAME_INPUT, test_data["name"])
        self.input_text(OrderPageLocators.LASTNAME_INPUT, test_data["lastname"])
        self.input_text(OrderPageLocators.ADDRESS_INPUT, test_data["address"])
        self.send_keys_to_input(OrderPageLocators.METRO_LOCATOR, test_data['metro'])
        self.wait_for_element(OrderPageLocators.ELEMENT_LIST_LOCATOR)
        self.click_on_element(OrderPageLocators.ELEMENT_LIST_LOCATOR)
        self.input_text(OrderPageLocators.PHONE_INPUT, test_data["phone"])
        self.click_on_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Заполнить форму 'Про аренду'")
    def fill_rental_form(self, rental_data):
        # Дата доставки
        self.input_text(OrderPageLocators.DELIVERY_DATE, rental_data["date"])

        # Срок аренды
        self.click_on_element(OrderPageLocators.RENTAL_PERIOD)
        self.click_on_element(OrderPageLocators.RENTAL_OPTIONS[rental_data["period"]])
        # Цвет самоката
        if rental_data.get("color") == "black":
            self.click_on_element(OrderPageLocators.COLOR_BLACK)
        elif rental_data.get("color") == "grey":
            self.click_on_element(OrderPageLocators.COLOR_GREY)
        # Комментарий
        if rental_data.get("comment"):
            self.input_text(OrderPageLocators.COMMENT, rental_data["comment"])
        # Подтверждение заказа
        self.click_on_element(OrderPageLocators.ORDER_BUTTON)

    @allure.step("Подтвердить заказ")
    def confirm_order(self):
        self.click_on_element(OrderPageLocators.CONFIRM_BUTTON)
        return self.is_element_visible(OrderPageLocators.SUCCESS_MODAL_HEADER)


    @allure.step("Проверить сообщение об успешном заказе")
    def verify_success_message(self):
        actual_text = self.get_text_on_element(OrderPageLocators.SUCCESS_MODAL_HEADER)
        return "Заказ оформлен" in actual_text

    @allure.step("Закрыть вкладку Куки")
    def accept_cookies(self):
        self.click_on_element(ButtonPageLocators.COOKIE_BUTTON)

