import pytest
from playwright.sync_api import Playwright, Page

@pytest.fixture(scope='session')
def initialize_browser_state(playwright: Playwright): # Фикстура для регистрации и сохранения пользователя

        # Открываем браузер и создаем новую страницу
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()  # Создание контекста
        page = context.new_page()

        # Переходим на страницу входа
        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

        # Заполняем поле email
        email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        email_input.fill("user.name@gmail.com")

        # Заполняем поле username
        password_input = page.get_by_test_id('registration-form-username-input').locator('input')
        password_input.fill("username")

        # Заполняем поле пароль
        password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        password_input.fill("password")

        # Нажимаем на кнопку Registration
        registration_button = page.get_by_test_id('registration-page-registration-button')
        registration_button.click()

        # Сохраняем данные пользователя в файл
        context.storage_state(path="browser-state.json")

        # Задержка для наглядности выполнения теста (не рекомендуется использовать в реальных тестах)
        page.wait_for_timeout(1000)

@pytest.fixture()
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Page: # Фикстура для загрузки сессии пользователя

        # Открываем браузер и создаем новую страницу
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state="browser-state.json")  # Указываем файл с сохраненным состоянием
        yield context.new_page()
        browser.close()
