
import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    #Список вопросов
    @allure.step("Открыть список вопросов")
    def open_question(self, question_number):
        question_locator = MainPageLocators.question_number(question_number)
        self.click_on_element(question_locator)

    @allure.step("Скролл до список вопросов")
    def scroll_question(self, question_number):
        scroll_to_element = MainPageLocators.question_number(question_number)
        self.scroll_to_element(scroll_to_element)


    @allure.step("Сравни текст ответа на вопросы о важном")
    def check_question_important(self, expected_text):
        actual_text = self.get_text_on_element(MainPageLocators.ANSWER_TO_IMPORTANT_QUESTIONS)
        return actual_text == expected_text

    @allure.step("Подождать загрузки списка вопросов")
    def wait_for_list_questions(self):
        self.wait_for_element(MainPageLocators.QUESTIONS_IMPORTANT)

    @allure.step("Закрыть вкладку Куки")
    def accept_cookies(self):
        self.click_on_element(MainPageLocators.COOKIE_BUTTON)

