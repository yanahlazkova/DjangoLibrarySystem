import json
import os
from faker import Faker

fake = Faker()


def json_handler(file_path, data=None):
    """
    Универсальная функция для чтения и записи данных в JSON-файл.

    Args:
        file_path (str): Путь к JSON-файлу.
        data (dict, optional): Словарь данных для записи. Если None, функция будет считывать данные.

    Returns:
        dict: Данные, считанные из файла, или None, если произошла ошибка.
    """
    # Если данные для записи не предоставлены, пытаемся их считать
    if data is None:
        if not os.path.exists(file_path):
            message = (f"Ошибка: Файл по пути '{file_path}' не найден.")
            return False, message

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return True, json.load(f)
        except json.JSONDecodeError:
            message = (f"Ошибка: Файл '{file_path}' содержит некорректный JSON-формат.")
            return False, message
        except Exception as e:
            message = (f"Произошла непредвиденная ошибка при чтении файла: {e}")
            return False, message

    # Если данные для записи предоставлены, пытаемся их записать
    else:
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            message = (f"Данные успешно записаны в файл '{file_path}'.")
            return True, message
        except Exception as e:
            message = (f"Произошла непредвиденная ошибка при записи файла: {e}")
            return False, message


def get_fake_id():
    return fake.org_id(long=True)
