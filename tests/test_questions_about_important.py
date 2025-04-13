import allure
import pytest

import data
from pages.main_page import MainPage

class TestQuestionsImportant:
    @allure.title("Проверка выпадающего списка в разделе Вопросы о важном")
    @pytest.mark.parametrize('question_number, expected_text', data.Data.answer_text)
    def test_dropdown_list(self, firefox_driver, question_number, expected_text):
        main_page = MainPage(firefox_driver)
        main_page.accept_cookies()
        main_page.scroll_question()
        main_page.wait_for_list_questions()
        main_page.wait_for_question_clickable(question_number)
        main_page.click_question(question_number)
        main_page.wait_for_answer_visible(question_number)
        assert main_page.check_question_important(expected_text)
