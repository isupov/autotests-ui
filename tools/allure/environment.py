import sys, platform

from config import settings


def create_allure_environment_file():
    # Создаем список из элементов в формате {key}={value}
    items = [f'{key}={value}' for key, value in settings.model_dump().items()]

    # Собираем все элементы в единую строку с переносами
    properties = '\n'.join(items)

    os_info = f"os_info={platform.system()}, {platform.release()}"
    python_version = f"python_version={sys.version}"

    full_content = '\n'.join([properties, os_info, python_version])

    # Открываем файл ./allure-results/environment.properties на чтение
    with open(settings.allure_results_dir.joinpath('environment.properties'), 'w+') as file:
        file.write(full_content)  # Записываем переменные в файл