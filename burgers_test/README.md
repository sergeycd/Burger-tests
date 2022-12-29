О проекте:
Данный проект проверяет работу сайта https://stellarburgers.nomoreparties.site/. 
Это космический фастфуд: можно собрать и заказать бургер из необычных ингредиентов.

Данные зарегестрированного пользователя:
Имя: Иван
Пароль: Qnt45LI
Логин: Space@mail.ru

# **Классы и их методы**

### TestRegistration

В данном классе я проверяю работу регистрации

#### TestRegistration.test_positiv_reg

Это позитивный кейс с регистрацией пользователя на сайте

#### TestRegistration.test_invalid_password

Проверка пользователя с невалидным паролем

#### TestRegistration.test_reg_witout_name

Проверка, что пользователь не сможет зарегестрироваться без имени


### TestAuth

Класс для проверки страниц входа и авторизации

#### TestAuth.test_auth_main_page

С основной страници

#### TestAuth.test_auth_account_page

С личного кабинета

#### TestAuth.test_auth_registration_page

Со страницы регистрации

#### TestAuth.test_auth_forgot_password_page

Со страницы восстановления пароля

### TestAccount
Класс для перехода в личный кабинет

#### test_move_to_account
Переход в личный кабинет


### TestConstructor
Класс для теста перехода к конструктору из личного кабинета

#### test_move_to_constructor_through
Метод для перехода к конструктору по клику на кнопку "конструктор"

#### test_move_to_constructor_through_burger
Метод для перехода к конструктору по клику на логотип "Бургера"

### TestExit
Класс для теста выхода из профиля

#### test_exit
Метод выхода из профия

### TestMenu
Класс для теста слайдеров меню

#### test_menu_bulki
Метод для проверки клика по слайдеру "булки"

#### test_menu_souse
Метод для проверки клика по слайдеру "соусы"

#### test_menu_nachinki
Метод для проверки клика по слайдеру "начинки"


# Локаторы

### Кнопки

Кнопка личный кабинет    
ACCOUNT = (By.CSS_SELECTOR, "a[href='/account']")

Кнопка войти/войти в аккаунт
LOG_IN = (By.XPATH, ".//button[contains(@class,'button_button__33qZ0')]")

Кнопка войти/войти в аккаунт
ENTER_BTN = (By.XPATH, '//*[@id="root"]/div/main/div/form/button')

Кнопка войти/войти в аккаунт
BTN_REG = (By.CSS_SELECTOR, ".button_button__33qZ0")

Кнопка войтив аккаунт
BTN_ENTER_MAIN = (By.XPATH, ".//button[text()='Войти в аккаунт']")

кнопка "Зарегестрироваться"
BTN_ENTER_LOGIN = (By.XPATH,".//form/button")

Кнопка личный кабинет 
BTN_ACCOUNT = (By.CSS_SELECTOR,"a[href='/account']")

Кнопка "Вход"
BTN_ENTER_REG = (By.CSS_SELECTOR,"a.Auth_link__1fOlj")

Кнопка "Оформить заказ"
BTN_OFFER = (By.XPATH,".//button[text()='Оформить заказ']")

кнопка "Конструктор" для перехода к конструктору
BTN_CONSTRUCTOR = (By.XPATH,".//p[text()='Конструктор']")

Заголовок/кнопка "Бургер" для перехода к конструктору
BTN_HEDER_BURGER = (By.XPATH, ".//nav/div/a")

Кнопка "Выход"
BTN_EXIT = (By.XPATH,".//nav//li[3]/button")

Кнопка "Булки"
BTN_BULKI = (By.XPATH,".//section/div[1]/div[1]/span")

Кнопка "Соусы"
BTN_SOUSE = (By.XPATH,".//section/div[1]/div[2]/span")

Кнопка "Начинка"
BTN_NUCHINKA = (By.XPATH,".//section/div[1]/div[3]/span")

"свободная кнопка"
BTN_FREE = (By.XPATH,".//div[@class='tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect'][1]/span")

Кнопка которая выбранна на данный момент
BTN_CHOSEN = (By.XPATH,".//div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']/span")

### Поля
Поле для ввода Email
EMAIL = (By.CSS_SELECTOR, "input[name = 'name']")

Поле для пароля
PASSWORD = (By.NAME, "Пароль")

Поле для ввода имени 
NAME_REG = (By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[1]/div/div/input")

Поле для ввода Email
EMAIL_REG = (By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[2]/div/div/input")

Поле для пароля
PASSWORD_REG = (By.CSS_SELECTOR, "input[name = 'Пароль']")

Поле для ввода Email
VALUE_EMAIL_REG = (By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[2]/div/div/input/@value")

Поле для ввода Email
VALUE_PASSWORD = (By.NAME, "Пароль")

Поле для ввода Email
FLD_EMAIL = (By.CSS_SELECTOR,"input[name='name']")

Поле для пароля
FLD_PASSWORD = (By.CSS_SELECTOR,"input[name='Пароль']")
### заголовки
Заголовок "Регистрация"
H2_REG = (By.XPATH, ".//main/div/h2")

Сообщение об ошибке "Некорректный пароль"
PASSWORD_ERROR = (By.CSS_SELECTOR, "p.input__error")

Заголовок профиль
HEAD_PROFILE = (By.CSS_SELECTOR,"a[href='/account/profile']")

Заголовок в конструкторе "Соберите бургер"
HEAD_CONSTRUCT = (By.XPATH,".//h1[text()='Соберите бургер']")

заголовок "Вход"
HEAD_ENTER = (By.XPATH,".//main//h2")

Заголовок "Булки"
HEAD_BULKI = (By.XPATH,".//h2[text()='Булки']")

Заголовок "Соус"
HEAD_SOUSE = (By.XPATH,".//h2[text()='Соусы']")

Заголовок "Начинки"
HEAD_NUCHINKA = (By.XPATH,".//h2[text()='Начинки']")


### Файлы
#### data.py
Файл где создали шаблон пользователя для теста с помощью @dataclass 
#### generator.py
Файл где генерирую данные для пользователей
#### locators_of_element.py
Файл с локаторами
#### base_page.py
Файл с методами для использования в тестах
#### element_pages.py
Файл с расписанными тестами
#### test_page.py
Файл с тестами
#### conftest.py
Фикстуры
#### requirements.txt
Файлы с импортами

