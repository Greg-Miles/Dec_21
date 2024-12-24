import json, csv

def read_json(file_path: str, encoding: str = "utf-8")-> str:
    """
    Описание:
    Читает данные из JSON-файла.
    Входные параметры:
    file_path: Путь к файлу.
    encoding: Кодировка файла (по умолчанию `"utf-8"`).
    Возвращаемое значение: Данные, считанные из файла.
    """
    with open(file_path, "r", encoding= encoding) as file:
        python_data = json.load(file)
    return python_data


def write_json(data: str, file_path: str, encoding: str = "utf-8")-> None:
    """
    Описание:
    Записывает данные в JSON-файл.
    Входные параметры:
    data: Данные для записи.
    file_path: Путь к файлу.
    encoding: Кодировка файла (по умолчанию `"utf-8"`).
    Возвращаемое значение: Нет.
    """
    with open(file_path, "w", encoding= encoding) as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def append_json(data: list[dict], file_path: str, encoding: str = "utf-8")-> None:
    """
    Описание:
    Добавляет данные в существующий JSON-файл.
    Входные параметры:
    data: Список словарей с данными для добавления.
    file_path: Путь к файлу.
    encoding: Кодировка файла (по умолчанию `"utf-8"`).
    Возвращаемое значение: Нет.
    """
    with open(file_path, "r", encoding= encoding) as file:
        python_data = json.load(file)
    if not isinstance(python_data, list):
        raise TypeError("Поддерживается только добавление в JSON массивы")

    python_data.extend(data)

    with open(file_path, "w", encoding= encoding) as file:
        json.dump(python_data, file, ensure_ascii= False, indent= 4)