import json, csv, yaml

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


def read_csv(file_path: str, delimiter=';', encoding: str ='windows-1251')-> list:
    """
    Описание: Читает данные из CSV-файла.
    Входные параметры:
    file_path: Путь к файлу.
    delimiter: Разделитель полей в файле (по умолчанию `';'`).
    encoding: Кодировка файла (по умолчанию `"windows-1251"`).
    Возвращаемое значение:
    Данные, считанные из файла.
    """
    input_list = []
    with open(file_path, "r", encoding= encoding) as file:
        reader = csv.DictReader(file, delimiter= delimiter)
        input_list = list(reader)
    return input_list


def write_csv(data: list, file_path: str, delimiter=';', encoding: str ='windows-1251')-> None:
    """
    Описание:
    Записывает данные в CSV-файл.
    Входные параметры:
    data: Данные для записи.
    file_path: Путь к файлу.
    delimiter: Разделитель полей в файле (по умолчанию `';'`).
    encoding: Кодировка файла (по умолчанию `"windows-1251"`).
    Возвращаемое значение:
    Нет.
    """
    with open(file_path, "w", encoding= encoding) as file:
        if  isinstance(data[0], dict):
            writer = csv.DictWriter(
            file, fieldnames=data[0].keys(), delimiter= delimiter, lineterminator="\n"
            )
            writer.writeheader()
            writer.writerows(data)
        if isinstance(data[0], list):
            writer = csv.writer(file, delimiter= delimiter, lineterminator="\n")
            writer.writerows(data)


def append_csv(data, file_path: str, delimiter=';', encoding: str ='windows-1251')-> None:
    """
    Описание: Добавляет данные в существующий CSV-файл.
    Входные параметры:
    data: Данные для добавления.
    file_path: Путь к файлу.
    delimiter: Разделитель полей в файле (по умолчанию `';'`).
    encoding: Кодировка файла (по умолчанию `"windows-1251"`).
    Возвращаемое значение:
    Нет.
    """
    with open(file_path, "a", encoding= encoding) as file:
        writer = csv.writer(file, delimiter= delimiter, lineterminator="\n")
        writer.writerow(data)


def read_txt(file_path: str, encoding: str = "utf-8")->list:
    """
    Описание:
    Читает данные из текстового файла.
    Входные параметры:
    file_path: Путь к файлу.
    encoding: Кодировка файла (по умолчанию `"utf-8"`).
    Возвращаемое значение:
    Содержимое файла.
    """
    with open(file_path, "r", encoding= encoding) as file:
        lines = file.readlines()
    return lines


def write_txt(data:str, file_path: str, encoding: str = "utf-8")-> None:
    """
    Описание: Записывает данные в текстовый файл.
    Входные параметры:
    data: Данные для записи.
    file_path: Путь к файлу.
    encoding: Кодировка файла (по умолчанию `"utf-8"`).
    Возвращаемое значение: 
    Нет.
    """
    with open(file_path, "w", encoding=encoding) as file:
        data.split("\n")
        file.write(data)


def append_txt(data: str, file_path: str, encoding: str = "utf-8")-> None:
    """
    Описание: Добавляет данные в конец текстового файла.
    Входные параметры:
    data: Данные для добавления.
    file_path: Путь к файлу.
    encoding: Кодировка файла (по умолчанию `"utf-8"`).
    Возвращаемое значение:
    Нет.
    """
    with open(file_path, "a", encoding=encoding) as file:
        file.write(data + "\n")


def read_yaml(file_path: str, encoding:str = "utf-8")->dict:
    """
    Описание: Читает данные из YAML-файла.
    Входные параметры:
    file_path: Путь к файлу.
    Возвращаемое значение:
    Данные, считанные из файла.
    """
    with open(file_path, 'r', encoding= encoding) as file:
        data = yaml.safe_load(file)
    return data

def write_yaml(data: dict, file_path: str, encoding:str = "utf-8")-> None:
    """
    Описание: Записывает данные в YAML-файл.
    Входные параметры:
    data: Данные для записи.
    file_path: Путь к файлу.
    Возвращаемое значение:
    Нет.
    """
    with open(file_path, 'w', encoding= encoding) as file:
        yaml.dump(data, file, allow_unicode=True, sort_keys=False, indent=4)


def main():
    pass


if __name__ == "__main__":
    main()