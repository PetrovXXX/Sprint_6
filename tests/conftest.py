import pytest
import requests
from selenium import webdriver

from curl import *
from data import Credentials


@pytest.fixture(scope="function")
def firefox_driver():
    browser = webdriver.Firefox()
    browser.get(main_site)
    yield browser
    browser.quit()

