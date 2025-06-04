import pytest
from playwright.sync_api import Page

from pages.login_page import LoginPage  # Импортируем LoginPage
from pages.registration_page import RegistrationPage  # Импортируем RegistrationPage

@pytest.mark.regression
@pytest.mark.authorization
@pytest.mark.parametrize("email, password", [
    ("user.name@gmail.com", "password"),
    ("user.name@gmail.com", "  "),
    ("  ", "password")
])
def test_wrong_email_or_password_authorization(login_page: LoginPage, email: str, password: str):
    login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
    login_page.fill_login_form(email=email, password=password)
    login_page.click_login_button()
    login_page.check_visible_wrong_email_or_password_alert()

@pytest.mark.regression
@pytest.mark.authorization
@pytest.mark.parametrize("email, username, password", [
    ("user.name@gmail.com", "username", "password")
])
def test_successful_registration(registration_page: RegistrationPage, email: str, username: str, password: str):
    registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    registration_page.fill_registration_form(email=email, username=username, password=password)
    registration_page.click_registration_button()