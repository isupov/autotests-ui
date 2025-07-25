import allure  # Импортируем allure
from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from elements.text import Text
from config import settings

class NavbarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.app_title = Text(page, 'navigation-navbar-app-title-text', 'Text')
        self.welcome_title = Text(page, 'navigation-navbar-welcome-title-text', 'Welcome Text')

    @allure.step("Check visible navigation bar")  # Добавили allure шаг
    def check_visible(self, username: str):
        self.app_title.check_visible()
        self.app_title.check_have_text('UI Course')

        self.welcome_title.check_visible()
        self.welcome_title.check_have_text(f'Welcome, {settings.test_user.username}!')