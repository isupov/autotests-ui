import re

from playwright.sync_api import Page

from pages.base_page import BasePage
from components.authentication.registration_form_component import RegistrationFormComponent
from elements.button import Button
from elements.link import Link

class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.registration_form = RegistrationFormComponent(page)
        self.registration_button = Button(page, 'registration-page-registration-button', 'Register Button')
        self.login_link = Link(page, 'registration-page-login-link', 'Login Link')

    def click_registration_button(self):
        self.registration_button.click()

    def click_login_link(self):
        self.login_link.click()
        # Добавили проверку
        self.check_current_url(re.compile(".*/#/auth/login"))