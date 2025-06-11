from playwright.sync_api import Page

from components.courses.courses_list_toolbar_view_component import CoursesListToolbarViewComponent
from components.courses.course_view_component import CourseViewComponent
from components.courses.course_view_menu_component import CourseViewMenuComponent
from components.views.empty_view_component import EmptyViewComponent
from components.navigation.navbar_component import NavbarComponent
from components.navigation.sidebar_component import SidebarComponent
from pages.base_page import BasePage

from elements.text import Text
from elements.button import Button


class CoursesListPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.navbar = NavbarComponent(page)

        self.sidebar = SidebarComponent(page)

        self.empty_view = EmptyViewComponent(page, 'courses-list')

        self.course_view = CourseViewComponent(page)

        # Добавили уже созданный компонент
        self.course_view_menu = CourseViewMenuComponent(page)

        self.toolbar_view = CoursesListToolbarViewComponent(page)

        self.courses_title = Text(page, 'courses-list-toolbar-title-text', 'Title' )
        self.create_course_button = Button(page, 'courses-list-toolbar-create-course-button', 'Button')

    def check_visible_courses_title(self):
        self.courses_title.check_visible()
        self.courses_title.check_have_text('Courses')

    def check_visible_empty_view(self):
        self.empty_view.check_visible(
            title='There is no results',
            description='Results from the load test pipeline will be displayed here'
        )