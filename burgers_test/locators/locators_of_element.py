from selenium.webdriver.common.by import By


# здесь указываем локаторы, после того как задали ожидание в Base_page
class AuthLocators:
    # buttons
    ACCOUNT = (By.CSS_SELECTOR, "a[href='/account']")
    LOG_IN = (By.XPATH, ".//button[contains(@class,'button_button__33qZ0')]")
    ENTER_BTN = (By.XPATH, '//*[@id="root"]/div/main/div/form/button')

    # fields
    EMAIL = (By.CSS_SELECTOR, "input[name = 'name']")
    PASSWORD = (By.NAME, "Пароль")


class RegLocators:
    # fields
    NAME_REG = (By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[1]/div/div/input")
    EMAIL_REG = (By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[2]/div/div/input")
    PASSWORD_REG = (By.CSS_SELECTOR, "input[name = 'Пароль']")
    VALUE_EMAIL_REG = (By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[2]/div/div/input/@value")
    # buttons
    BTN_REG = (By.CSS_SELECTOR, ".button_button__33qZ0")
    # to assert
    VALUE_EMAIL = (By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[1]/div/div/input")
    VALUE_PASSWORD = (By.NAME, "Пароль")
    H2_REG = (By.XPATH, ".//main/div/h2")
    # password errors
    PASSWORD_ERROR = (By.CSS_SELECTOR, "p.input__error")


class LoginLocators:
    # fields
    FLD_EMAIL = (By.CSS_SELECTOR,"input[name='name']")
    FLD_PASSWORD = (By.CSS_SELECTOR,"input[name='Пароль']")
    # buttons
    BTN_ENTER_MAIN = (By.XPATH, ".//button[text()='Войти в аккаунт']")
    BTN_ENTER_LOGIN = (By.XPATH,".//form/button")
    BTN_ACCOUNT = (By.CSS_SELECTOR,"a[href='/account']")
    BTN_ENTER_REG = (By.CSS_SELECTOR,"a.Auth_link__1fOlj")
    # to assert
    BTN_OFFER = (By.XPATH,".//button[text()='Оформить заказ']")
    HEAD_PROFILE = (By.CSS_SELECTOR,"a[href='/account/profile']")
    # password errors

class Constructor:
    # fields
    FLD_EMAIL = (By.CSS_SELECTOR,"input[name='name']")
    FLD_PASSWORD = (By.CSS_SELECTOR,"input[name='Пароль']")
    # buttons
    BTN_ACCOUNT = (By.CSS_SELECTOR, "a[href='/account']")
    BTN_ENTER_LOGIN = (By.XPATH, ".//form/button")
    BTN_CONSTRUCTOR = (By.XPATH,".//p[text()='Конструктор']")
    BTN_HEDER_BURGER = (By.XPATH, ".//nav/div/a")
    #for assert
    HEAD_CONSTRUCT = (By.XPATH,".//h1[text()='Соберите бургер']")

class ExitLocators:
    # fields
    FLD_EMAIL = (By.CSS_SELECTOR,"input[name='name']")
    FLD_PASSWORD = (By.CSS_SELECTOR,"input[name='Пароль']")
    # buttons
    BTN_ACCOUNT = (By.CSS_SELECTOR, "a[href='/account']")
    BTN_ENTER_LOGIN = (By.XPATH, ".//form/button")
    BTN_EXIT = (By.XPATH,".//nav//li[3]/button")
    BTN_ACCOUNT = (By.CSS_SELECTOR, "a[href='/account']")
    #for assurt
    HEAD_ENTER = (By.XPATH,".//main//h2")

class MenuLocators:
    #buttons
    BTN_BULKI = (By.XPATH,".//section/div[1]/div[1]/span")
    BTN_SOUSE = (By.XPATH,".//section/div[1]/div[2]/span")
    BTN_NUCHINKA = (By.XPATH,".//section/div[1]/div[3]/span")
    BTN_FREE = (By.XPATH,".//div[@class='tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect'][1]/span")
    BTN_CHOSEN = (By.XPATH,".//div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']/span")
    #for assurt
    HEAD_BULKI = (By.XPATH,".//h2[text()='Булки']")
    HEAD_SOUSE = (By.XPATH,".//h2[text()='Соусы']")
    HEAD_NUCHINKA = (By.XPATH,".//h2[text()='Начинки']")

