import pytest

from pages.registration_page import RegistrationPage  # Импортируем RegistrationPage
from pages.dashboard_page import DashboardPage # Импортируем DashboardPage


@pytest.mark.regression
@pytest.mark.authorization
def test_successful_registration(dashboard_page: DashboardPage, registration_page: RegistrationPage, email: str, username: str, password: str):
    registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    registration_page.fill_registration_form( email="user.name@gmail.com",
        username="username",
        password="password")
    registration_page.click_registration_button()
    dashboard_page.check_dashboard_title()