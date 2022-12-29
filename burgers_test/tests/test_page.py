import time

from pages.element_pages import TextLocators, RegistrationPage, AuthPage, AccountPage, ConstructorPage, ExitPage, \
    MenuPage


class TestEl:
    class TestTextLocators:
        def test(self,driver):
            # здесь создаем переменную в котрую засовываем  класс из element_page содержащий элементы для данного теста
            page = TextLocators(driver, 'https://stellarburgers.nomoreparties.site/')
            page.open()
            page.log_in_click()
            time.sleep(3)
    # создаем класс для теста регистрации
    class TestRegistration:
        # в аргумент функции засовываем фикстуру driver
        def test_positiv_reg(self, driver):
            # здесь создаем переменную в котрую засовываем  класс из element_page содержащий элементы для данного теста
            reg_page_pr = RegistrationPage(driver, 'https://stellarburgers.nomoreparties.site/register')
            #открываем страницу с помощью метода Base_page.open, который является аргументом у класса RegistrationPage
            reg_page_pr.open()
            # здесь используем методы класса RegistrationPage
            reg_page_pr.registration_with_valid_data()


        # здесь мы проверим валидацию пароля на значения ниже 6 символов
        # в аргумент функции засовываем фикстуру driver
        def test_invalid_password(self, driver):
            # здесь создаем переменную в котрую засовываем  класс из element_page содержащий элементы для данного теста
            reg_page_ip = RegistrationPage(driver, 'https://stellarburgers.nomoreparties.site/register')
            # открываем страницу с помощью метода Base_page.open, который является аргументом у класса RegistrationPage
            reg_page_ip.open()
            # здесь используем методы класса RegistrationPage
            reg_page_ip.registration_with_invalid_password()

        # в аргумент функции засовываем фикстуру driver
        # здесь проверим что без имени регистрация не пройдет
        def test_reg_witout_name(self,driver):
            # здесь создаем переменную в котрую засовываем  класс из element_page содержащий элементы для данного теста
            reg_page_wn = RegistrationPage(driver,'https://stellarburgers.nomoreparties.site/register')
            # открываем страницу с помощью метода Base_page.open, который является аргументом у класса RegistrationPage
            reg_page_wn.open()
            # здесь используем методы класса RegistrationPage
            reg_page_wn.registration_without_name()

    # в данном классе я тестирую вход с разных страниц
    class TestAuth:
        # с основной страници
        def test_auth_main_page(self,driver):
             # здесь создаем переменную в котрую засовываем  класс из element_page содержащий элементы для данного теста
             auth_page_mp = AuthPage(driver,"https://stellarburgers.nomoreparties.site/")
             auth_page_mp.open()
             auth_page_mp.auth_main_page()


        # с личного кабинета
        def test_auth_account_page(self,driver):
            auth_page_ap = AuthPage(driver,"https://stellarburgers.nomoreparties.site/")
            auth_page_ap.open()
            auth_page_ap.auth_account_page()

        # со страницы регистрации
        def test_auth_registration_page(self,driver):
            auth_page_rp = AuthPage(driver,"https://stellarburgers.nomoreparties.site/register")
            auth_page_rp.open()
            auth_page_rp.auth_registration_page()

        #  со страницы восстановления пароля
        def test_auth_forgot_password_page(self,driver):
            auth_page_fpp = AuthPage(driver,"https://stellarburgers.nomoreparties.site/forgot-password")
            auth_page_fpp.open()
            auth_page_fpp.auth_forgot_password_page()

    # переход в личный кабинет
    class TestAccount:
        # (5)добавили фикстуру в аргумент метода и в аргумент самого метода из element_pages
        def test_move_to_account(self,driver, site_user):
            move_to_account = AccountPage(driver,"https://stellarburgers.nomoreparties.site/")
            move_to_account.open()
            move_to_account.move_to_account(site_user)
            time.sleep(1)
    # переход в конструктор
    class TestConstructor:
        #  переход по клику на "конструктор"
        def test_move_to_constructor_through(self,driver, site_user):
            move_to_constructor = ConstructorPage(driver,"https://stellarburgers.nomoreparties.site/login")
            move_to_constructor.open()
            move_to_constructor.move_to_constructor(site_user)
            time.sleep(1)

        def test_move_to_constructor_through_burger(self,driver, site_user):
            move_to_constructor = ConstructorPage(driver,"https://stellarburgers.nomoreparties.site/login")
            move_to_constructor.open()
            move_to_constructor.move_to_constructor_with_header(site_user)


    class TestExit:
        def test_exit(self, driver,site_user):
            exit = ExitPage(driver,"https://stellarburgers.nomoreparties.site/login")
            exit.open()
            exit.exit_from_account(site_user)
            time.sleep(1)

    class TestMenu:
        def test_menu_bulki(self, driver):
            open_page = MenuPage(driver, "https://stellarburgers.nomoreparties.site/")
            open_page.open()
            open_page.move_to_bulki()

        def test_menu_souse(self, driver):
            open_page = MenuPage(driver, "https://stellarburgers.nomoreparties.site/")
            open_page.open()
            open_page.move_to_souse()

        def test_menu_nachinki(self, driver):
            open_page = MenuPage(driver, "https://stellarburgers.nomoreparties.site/")
            open_page.open()
            open_page.move_to_nachinki()








