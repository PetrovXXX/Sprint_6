from selenium.webdriver.common.by import By


class MainPageLocators:
    BUTTON_HOME_PAGE_SCOOTER = (By.XPATH, './/img[@alt="Scooter"]') # Кнопка Самокат
    BUTTON_HOME_PAGE_DZEN = (By.XPATH, './/img[@alt="Yandex"]') # Кнопка Яндекс(Дзен)
    QUESTIONS_IMPORTANT = (By.XPATH, '//div[@class="Home_FourPart__1uthg"]') # Раздел Вопросы о важном
    ANSWER_TO_IMPORTANT_QUESTIONS = (By.XPATH, "//div[@class='accordion__panel' and not(@hidden)]") #Ответы на вопросы о важном
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")


    @staticmethod
    def question_number(question):
        return By.XPATH, f'//div[contains(@id, "accordion__panel-{question}")'

    @staticmethod
    def question_locator(question_number):
        return By.XPATH, f'//div[@id="accordion__heading-{question_number}"]'

    @staticmethod
    def answer_locator(question_number):
        return By.XPATH, f'//div[@id="accordion__panel-{question_number}"]/p'
