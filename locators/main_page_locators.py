from selenium.webdriver.common.by import By


class MainPageLocators:
    BUTTON_HOME_PAGE_SCOOTER = (By.XPATH, './/img[@alt="Scooter"]') # Кнопка Самокат
    BUTTON_HOME_PAGE_DZEN = (By.XPATH, './/img[@alt="Yandex"]') # Кнопка Яндекс(Дзен)
    QUESTIONS_IMPORTANT = (By.XPATH, './/div[@class="accordion"]') # Раздел Вопросы о важном
    ANSWER_TO_IMPORTANT_QUESTIONS = (By.XPATH, "//div[@class='accordion__panel' and not(@hidden)]") #Ответы на вопросы о важном
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")


    @staticmethod
    def question_number(question):
        return By.XPATH, f'//*[@id="root"]/div/div/div[5]/div[2]/div/div[{question}]'
