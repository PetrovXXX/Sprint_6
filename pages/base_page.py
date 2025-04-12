import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Подождать видимости элемента")
    def wait_for_element(self, locator, timeout=55):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step("Скролл до элемента")
    def scroll_to_element(self, locator, timeout=55):
        element = self.wait_for_element(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Кликнуть на элемент")
    def click_on_element(self, locator, timeout=55):
        element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    @allure.step("Ввести текст в поле ввода")
    def send_keys_to_input(self, locator, text, timeout=30):
        element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    @allure.step("Получить текст элемента")
    def get_text_on_element(self, locator, timeout=15):
        element = self.wait_for_element(locator, timeout)
        return element.text

    @allure.step("Подождать и проверить, что атрибут элемента содержит текст")
    def wait_for_attribute(self, locator, attribute, value, timeout=15):
        return WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element_attribute(locator, attribute, value))

    @allure.step("Подождать элемент и ввести тест")
    def input_text(self, locator, text, timeout=25):
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator)).send_keys(text)

    @allure.step("Подождать пока текст станет видимым")
    def is_element_visible(self, locator, timeout=10):
        visible = self.wait_for_element(locator, timeout)
        return visible.is_displayed()

    @allure.step("Подождать пока откроется страница в новой вкладке")
    def redirect_dzen_url(self, expected_url_part, timeout=15):
        self.driver.switch_to.window(self.driver.window_handles[1])
        # Ждем загрузки URL
        WebDriverWait(self.driver, timeout).until(EC.url_contains(expected_url_part))
        # Получаем текущий URL
        current_url = self.driver.current_url
        return current_url

    @allure.step("Подождать пока откроется страница")
    def open_web_page(self, url, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.url_contains(url))
        return self.driver.current_url

    @allure.step("Проскроллить до элемента")
    def scroll_to_element_with_centering(self, locator, timeout=40):
        element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});", element)
        return element

    @allure.step("Кликнуть на элемент отцентровано")
    def click_on_element_with_centering(self, locator, timeout=40):
        element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});", element)
        element.click()
