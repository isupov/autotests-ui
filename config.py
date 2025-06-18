import sys, platform

from enum import Enum
from typing import Self

from pydantic import EmailStr, FilePath, HttpUrl, DirectoryPath
from pydantic_settings import BaseSettings, SettingsConfigDict


class Browser(str, Enum):
    WEBKIT = "webkit"
    FIREFOX = "firefox"
    CHROMIUM = "chromium"


class TestUser(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="TEST_USER")

    email: EmailStr
    username: str
    password: str


class TestData(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="TEST_DATA")

    image_png_file: FilePath


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_nested_delimiter=".",
    )

    app_url: HttpUrl
    headless: bool
    browsers: list[Browser]
    test_user: TestUser
    test_data: TestData
    videos_dir: DirectoryPath
    tracing_dir: DirectoryPath
    allure_results_dir: DirectoryPath  # Добавили новое поле
    browser_state_file: FilePath
    os_info: str
    python_version: str


    def get_base_url(self) -> str:
        return f"{self.app_url}/"

    @classmethod
    def initialize(cls) -> Self:
        videos_dir = DirectoryPath("./videos")
        tracing_dir = DirectoryPath("./tracing")
        allure_results_dir = DirectoryPath("./allure-results")  # Создаем объект пути к папке
        browser_state_file = FilePath("browser-state.json")
        os_info = f"{platform.system()}, {platform.release()}"
        python_version = sys.version

        videos_dir.mkdir(exist_ok=True)
        tracing_dir.mkdir(exist_ok=True)
        allure_results_dir.mkdir(exist_ok=True)  # Создаем папку allure-results, если она не существует
        browser_state_file.touch(exist_ok=True)

        return Settings(
            videos_dir=videos_dir,
            tracing_dir=tracing_dir,
            allure_results_dir=allure_results_dir,  # Передаем allure_results_dir в инициализацию настроек
            browser_state_file=browser_state_file,
            os_info=os_info,
            python_version=python_version,
        )


settings = Settings.initialize()