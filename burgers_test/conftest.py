import pytest
from selenium import webdriver

from generator.generator import UserSite


# cjplftncz d gthde. jxthtlm abrcnehf c lhfqdthjv
@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope='function')
# (2)наполнили данными класс созданный в generator пердварительно его импортировав,далее использовали данную фикстуру
# в методе в element_pages
def site_user():
    us = UserSite(name = "Иван",login = "Space@mail.ru",password = "Qnt45LI")
    return us
    # class UserSite:
    #     name = "Иван"
    #     login = "Space@mail.ru"
    #     password = "Qnt45LI"


