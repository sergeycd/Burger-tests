
from generator.generator import generate_person_with_valid_data, generate_person_with_failing_password, UserSite
from locators.locators_of_element import AuthLocators, RegLocators, LoginLocators, Constructor, ExitLocators, \
    MenuLocators
from pages.base_page import BasePage


# Добавляем как аргумент основную страницу(BasePage) с методами, которая будет запускать страницу и устанавливать драйвер
# ожидания и элементы которые мы в этих методах используем, делаем после того как укажем локаторы для элементов
class TextLocators(BasePage):
    # подтягиваем класс с локаторами для данного теста из locators_of_element
    locators = AuthLocators

    def log_in_click(self):
        #добавляю сюда данные из generator.py
        # в первой строке ставлю итератор next что бы данные подставились корректно
        iterator = next(generate_person_with_valid_data())
        email = iterator.email
        password = iterator.password
        user_name = iterator.user_name
        self.element_is_visible(self.locators.LOG_IN).click()
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.PASSWORD).send_keys(password)
        self.element_is_visible(self.locators.ENTER_BTN).click()

# Добавляем как аргумент основную страницу(BasePage) с методами, которая будет запускать страницу и устанавливать драйвер
# ожидания и элементы которые мы в этих методах используем, делаем после того как укажем локаторы для элементов
class RegistrationPage(BasePage):
    # подтягиваем класс с локаторами для данного теста из locators_of_element
    reg_locators = RegLocators()

    def registration_with_valid_data(self):
        # создаем переменную в которую засовываем генератор пользователя и перед ним ставим next
        iterator = next(generate_person_with_valid_data())
        # ниже используем создаем данные пользователю для теста
        email = iterator.email
        password = iterator.password_valid
        name_of_user = iterator.user_name
        self.element_is_visible(self.reg_locators.NAME_REG).send_keys(name_of_user)
        self.element_is_visible(self.reg_locators.EMAIL_REG).send_keys(email)
        self.element_is_visible(self.reg_locators.PASSWORD_REG).send_keys(password)
        rtr = self.element_is_visible(self.reg_locators.PASSWORD_REG).get_attribute('value')
        self.element_is_visible(self.reg_locators.BTN_REG).click()
        trt = self.element_is_visible(self.reg_locators.VALUE_PASSWORD).get_attribute('value')


        assert trt == rtr


    def registration_with_invalid_password(self):
        # создаем переменную в которую засовываем генератор пользователя(класс) и перед ним ставим next
        iterator = next(generate_person_with_failing_password())
        # ниже используем создаем данные пользователю для теста
        email = iterator.email
        password = iterator.password
        name_of_user = iterator.user_name
        self.element_is_visible(self.reg_locators.NAME_REG).send_keys(name_of_user)
        self.element_is_visible(self.reg_locators.EMAIL_REG).send_keys(email)
        self.element_is_visible(self.reg_locators.PASSWORD_REG).send_keys(password)
        self.element_is_visible(self.reg_locators.BTN_REG).click()
        assert self.element_is_visible(self.reg_locators.PASSWORD_ERROR).text == "Некорректный пароль"

    def registration_without_name(self):
        # создаем переменную в которую засовываем генератор пользователя(класс) и перед ним ставим next
        iterator = next(generate_person_with_valid_data())
        # ниже используем создаем данные пользователю для теста
        email = iterator.email
        password = iterator.password
        name_of_user = iterator.user_name
        self.element_is_visible(self.reg_locators.EMAIL_REG).send_keys(email)
        self.element_is_visible(self.reg_locators.PASSWORD_REG).send_keys(password)
        self.element_is_visible(self.reg_locators.BTN_REG).click()

        assert self.element_is_visible(self.reg_locators.H2_REG).text == "Регистрация"

class AuthPage(BasePage):

    auth_locators = LoginLocators()

    name = "Иван"
    login = "Space@mail.ru"
    password = "Qnt45LI"
    def auth_main_page(self):
        self.element_is_visible(self.auth_locators.BTN_ENTER_MAIN).click()
        self.element_is_visible(self.auth_locators.FLD_EMAIL).send_keys(self.login)
        self.element_is_visible(self.auth_locators.FLD_PASSWORD).send_keys(self.password)
        self.element_is_visible(self.auth_locators.BTN_ENTER_LOGIN).click()
        assert self.element_is_visible(self.auth_locators.BTN_OFFER).text == "Оформить заказ"

    def auth_account_page(self):
        self.element_is_visible(self.auth_locators.BTN_ACCOUNT).click()
        self.element_is_visible(self.auth_locators.FLD_EMAIL).send_keys(self.login)
        self.element_is_visible(self.auth_locators.FLD_PASSWORD).send_keys(self.password)
        self.element_is_visible(self.auth_locators.BTN_ENTER_LOGIN).click()
        assert self.element_is_visible(self.auth_locators.BTN_OFFER).text == "Оформить заказ"

    def auth_registration_page(self):
        self.element_is_visible(self.auth_locators.BTN_ENTER_REG).click()
        self.element_is_visible(self.auth_locators.FLD_EMAIL).send_keys(self.login)
        self.element_is_visible(self.auth_locators.FLD_PASSWORD).send_keys(self.password)
        self.element_is_visible(self.auth_locators.BTN_ENTER_LOGIN).click()
        assert self.element_is_visible(self.auth_locators.BTN_OFFER).text == "Оформить заказ"

    def auth_forgot_password_page(self):
        self.element_is_visible(self.auth_locators.BTN_ENTER_REG).click()
        self.element_is_visible(self.auth_locators.FLD_EMAIL).send_keys(self.login)
        self.element_is_visible(self.auth_locators.FLD_PASSWORD).send_keys(self.password)
        self.element_is_visible(self.auth_locators.BTN_ENTER_LOGIN).click()
        assert self.element_is_visible(self.auth_locators.BTN_OFFER).text == "Оформить заказ"

class AccountPage(BasePage):
    login_locators = LoginLocators()


    # (4) добавили фикстуру в аргументы метода
    def move_to_account(self, site_user):

        self.element_is_visible(self.login_locators.BTN_ENTER_MAIN).click()
        self.element_is_visible(self.login_locators.FLD_EMAIL).send_keys(site_user.login)
        self.element_is_visible(self.login_locators.FLD_PASSWORD).send_keys(site_user.password)
        self.element_is_visible(self.login_locators.BTN_ENTER_LOGIN).click()
        self.element_is_visible(self.login_locators.BTN_ACCOUNT).click()
        assert self.element_is_visible(self.login_locators.HEAD_PROFILE).text == 'Профиль'



class ConstructorPage(BasePage):
    construct_locators = Constructor()

    def move_to_constructor(self, site_user):

        self.element_is_visible(self.construct_locators.FLD_EMAIL).send_keys(site_user.login)
        self.element_is_visible(self.construct_locators.FLD_PASSWORD).send_keys(site_user.password)
        self.element_is_visible(self.construct_locators.BTN_ENTER_LOGIN).click()
        self.element_is_visible(self.construct_locators.BTN_ACCOUNT).click()
        self.element_is_visible(self.construct_locators.BTN_CONSTRUCTOR).click()
        assert self.element_is_visible(self.construct_locators.HEAD_CONSTRUCT).text == 'Соберите бургер'

    def move_to_constructor_with_header(self, site_user):

        self.element_is_visible(self.construct_locators.FLD_EMAIL).send_keys(site_user.login)
        self.element_is_visible(self.construct_locators.FLD_PASSWORD).send_keys(site_user.password)
        self.element_is_visible(self.construct_locators.BTN_ENTER_LOGIN).click()
        self.element_is_visible(self.construct_locators.BTN_ACCOUNT).click()
        self.element_is_visible(self.construct_locators.BTN_HEDER_BURGER).click()
        assert self.element_is_visible(self.construct_locators.HEAD_CONSTRUCT).text == 'Соберите бургер'


class ExitPage(BasePage):
    exit_locators = ExitLocators()

    def exit_from_account(self, site_user):
        self.element_is_visible(self.exit_locators.FLD_EMAIL).send_keys(site_user.login)
        self.element_is_visible(self.exit_locators.FLD_PASSWORD).send_keys(site_user.password)
        self.element_is_visible(self.exit_locators.BTN_ENTER_LOGIN).click()
        self.element_is_visible(self.exit_locators.BTN_ACCOUNT).click()
        self.element_is_visible(self.exit_locators.BTN_EXIT).click()
        assert self.element_is_visible(self.exit_locators.HEAD_ENTER).text == 'Вход'

class MenuPage(BasePage):
    menu_locators = MenuLocators()

    def move_to_bulki(self):
        if self.element_is_visible(self.menu_locators.BTN_CHOSEN).text == "Булки":
            self.element_is_visible(self.menu_locators.BTN_SOUSE).click()
            self.element_is_visible(self.menu_locators.BTN_BULKI).click()
        else:
            self.element_is_visible(self.menu_locators.BTN_BULKI).click()
        assert self.element_is_visible(self.menu_locators.HEAD_BULKI).text == "Булки"

    def move_to_souse(self):
        if self.element_is_visible(self.menu_locators.BTN_CHOSEN).text == "Соусы":
            self.element_is_visible(self.menu_locators.BTN_BULKI).click()
            self.element_is_visible(self.menu_locators.BTN_SOUSE).click()
        else:
            self.element_is_visible(self.menu_locators.BTN_SOUSE).click()
        assert self.element_is_visible(self.menu_locators.HEAD_SOUSE).text == "Соусы"

    def move_to_nachinki(self):
        if self.element_is_visible(self.menu_locators.BTN_CHOSEN).text == "Начинки":
            self.element_is_visible(self.menu_locators.BTN_SOUSE).click()
            self.element_is_visible(self.menu_locators.BTN_NUCHINKA).click()
        else:
            self.element_is_visible(self.menu_locators.BTN_NUCHINKA).click()

        assert self.element_is_visible(self.menu_locators.HEAD_NUCHINKA).text == "Начинки"

















