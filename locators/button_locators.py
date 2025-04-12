from selenium.webdriver.common.by import By

class ButtonPageLocators:
    ORDER_BUTTON_ABOVE = (By.XPATH, './/button[@class="Button_Button__ra12g"]')  # Кнопка заказать сверху
    ORDER_BUTTON_BELOW = (By.XPATH, './/button[@class="Button_Button__ra12g Button_UltraBig__UU3Lp"]')  # Кнопка заказать №2 снизу
    BUTTON_HOME_PAGE_SCOOTER = (By.XPATH, './/img[@alt="Scooter"]')  # Кнопка Самокат
    BUTTON_HOME_PAGE_DZEN = (By.XPATH, './/img[@alt="Yandex"]')  # Кнопка Яндекс(Дзен)
    QUESTIONS_IMPORTANT = (By.XPATH, './/div[@class="accordion"]')  # Раздел Вопросы о важном
    ANSWER_TO_IMPORTANT_QUESTIONS = (
    By.XPATH, "//div[@class='accordion__panel' and not(@hidden)]")  # Ответы на вопросы о важном
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")

    @staticmethod
    def button_order_bot():
        order_button_above = By.XPATH, f'//*[@id="root"]/div/div/div[4]/div[2]/div[5]/button'
        return order_button_above

