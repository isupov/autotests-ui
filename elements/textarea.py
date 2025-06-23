import allure  # Импортируем allure
from playwright.sync_api import Locator, expect
from ui_coverage_tool import ActionType


from elements.base_element import BaseElement

from tools.logger import get_logger  # Импортируем get_logger

logger = get_logger("TEXTAREA_ELEMENT")  # Инициализируем logger

class Textarea(BaseElement):
    @property
    def type_of(self) -> str:  # Переопределяем свойство type_of
        return "textarea"

    def get_locator(self, nth: int = 0, **kwargs) -> Locator:
        return super().get_locator(nth, **kwargs).locator('textarea').first

    def get_raw_locator(self, nth: int = 0, **kwargs) -> str:
        # Возвращает строковое XPath-представление локатора для покрытия.
        # Важно: Playwright сам не даёт доступ к исходному локатору, поэтому мы формируем его вручную.
        # Используем XPath, так как он легко поддерживает индексацию ([n+1]).
        return f"//*[@data-testid='{self.locator.format(**kwargs)}'][{nth + 1}]"

    def fill(self, value: str, nth: int = 0, **kwargs):
        step = f'Fill {self.type_of} "{self.name}" to value "{value}"'

        with allure.step(step):  # Добавили шаг
            logger.info(step)
            locator = self.get_locator(nth, **kwargs)
            locator.fill(value)

        self.track_coverage(ActionType.FILL, nth, **kwargs)


    def check_have_value(self, value: str, nth: int = 0, **kwargs):
        step = f'Checking that {self.type_of} "{self.name}" has a value "{value}"'

        with allure.step(step):  # Добавили шаг
            logger.info(step)
            locator = self.get_locator(nth, **kwargs)
            expect(locator).to_have_value(value)

        self.track_coverage(ActionType.VALUE, nth, **kwargs)