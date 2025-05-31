from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
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

    # Проверяем, что не появилось сообщение об ошибке
    dashboard_title = page.get_by_test_id('dashboard-toolbar-title-text')
    expect(dashboard_title).to_be_visible()
    expect(dashboard_title).to_have_text("Dashboard")

    # Задержка для наглядности выполнения теста (не рекомендуется использовать в реальных тестах)
    page.wait_for_timeout(5000)

with sync_playwright() as playwright:
    # Открываем браузер и создаем новую страницу
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="browser-state.json")  # Указываем файл с сохраненным состоянием
    page = context.new_page()

    # Переходим на страницу входа
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    # Проверяем  наличие и текст заголовков "Courses", "There is no results"
    courses_title = page.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_title).to_be_visible()
    expect(courses_title).to_have_text("Courses")

    courses_title = page.get_by_test_id('courses-list-empty-view-title-text')
    expect(courses_title).to_be_visible()
    expect(courses_title).to_have_text("There is no results")

    # Задержка для наглядности выполнения теста (не рекомендуется использовать в реальных тестах)
    page.wait_for_timeout(5000)

