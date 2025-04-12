from selenium.webdriver.common.by import By

class OrderPageLocators:
    ORDER_BUTTON_ABOVE = (By.XPATH, './/button[@class="Button_Button__ra12g"]') #Кнопка заказать сверху
    ORDER_BUTTON_BELOW = (By.XPATH, '///button[@class="Button_Button__ra12g Button_UltraBig__UU3Lp"]') # Кнопка заказать №2 снизу
    #Форма заказа
    ORDER_BUTTON_HEADER = (By.XPATH, "//button[contains(text(), 'Заказать') and contains(@class, 'Button_Button__ra12g')]")
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    LASTNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    DROPDOWN_LOCATOR = (By.CLASS_NAME, "select-search__select")
    METRO_LOCATOR = (By.XPATH, "//input[@placeholder='* Станция метро']")
    ELEMENT_LIST_LOCATOR = (By.XPATH, "//li[@class='select-search__row']")

    @staticmethod
    def station_locator(station_name):
     return By.XPATH, f"//div[contains(@class, 'select-search__option') and text()='{station_name}']"


    #Про Аренду
    DELIVERY_DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    DATE_LIST = (By.CLASS_NAME, "react-datepicker__day react-datepicker__day--021 react-datepicker__day--selected")
    CLICK_DATE = (By.CLASS_NAME, "Dropdown-option")

    RENTAL_PERIOD = (By.CLASS_NAME, "Dropdown-arrow")
    RENTAL_OPTIONS = {
        'сутки': (By.XPATH, "//div[text()='сутки']"),
        'двое суток': (By.XPATH, "//div[text()='двое суток']"),

    }
    COLOR_BLACK = (By.ID, "black")
    COLOR_GREY = (By.ID, "grey")
    COMMENT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Middle') and text()='Заказать']")
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Да']")
    SUCCESS_MODAL_HEADER = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader')]")
