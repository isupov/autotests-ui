import pytest
import allure
from allure_commons.types import Severity # Импортируем enum Severity из Allure

from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage
from pages.authentication.login_page import LoginPage
from tools.allure.epics import AllureEpic # Импортируем enum AllureEpic
from tools.allure.features import AllureFeature # Импортируем enum AllureFeature
from tools.allure.stories import AllureStory # Импортируем enum AllureStory
from tools.allure.tags import AllureTag


@pytest.mark.regression
@pytest.mark.registration
@allure.tag(AllureTag.REGRESSION, AllureTag.REGISTRATION)
@allure.epic(AllureEpic.LMS) # Добавили epic
@allure.feature(AllureFeature.AUTHENTICATION) # Добавили feature
@allure.story(AllureStory.REGISTRATION) # Добавили story
class TestRegistration:
    @allure.title("Registration with correct email, username and password") # Добавили заголовок
    @allure.severity(Severity.CRITICAL) # Добавили severity
    def test_successful_registration(self, dashboard_page: DashboardPage, registration_page: RegistrationPage):
        registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
        registration_page.registration_form.fill(
            email="user.name@gmail.com",
            username="username",
            password="password"
        )
        registration_page.click_registration_button()

        dashboard_page.dashboard_toolbar.check_visible()
