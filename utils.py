import json

from datetime import datetime


def get_data():
    """
    Считывает информацию с файла operations.json
    """
    with open("operations.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def get_executed_operations(data):
    """
    Проверяет каждый элемент в спсике на наличие ключа "state"
    Если есть, то проверяет чтобы значение к ключу было "EXECUTED"
    Возвращает спсок с подходящими эелементами
    """
    filtered_data = []
    for item in data:
        if "state" in item:
            if item["state"] == "EXECUTED":
                filtered_data.append(item)
    return filtered_data


def get_last_operations(data, count_last_operations):
    """
    Сортирует спски по дате
    Возвращает последние несколько операций по дате
    """
    data = sorted(data, key=lambda item: item["date"], reverse=True)
    data = data[:count_last_operations]
    return data


def encode_bill(bill_info):
    """
    Делит информацию о счете или карте по названию и номеру
    Шифрует номер карты или счета, заменяя часть цифр на *
    Возвращает зашифрованные данные
    """
    bill_info = bill_info.split()
    bill, info = bill_info[-1], "".join(bill_info[:-1])
    if len(bill) == 16:
        bill = f"{ bill[:4] } { bill[4:6] }** **** { bill[-4:] }"
    else:
        bill = f"**{ bill[-4:] }"

    to = f"{ info } { bill }"
    return to


def get_data_format(data):
    """
    Для каждого элемента в списке меняет формат даты
    Возвращает информацию об операциях в удобном формате
    """
    formatted_data = []
    for item in data:
        date = datetime.strptime(item["date"], "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
        description = item["description"]
        if "from" in item:
            sender = encode_bill(item["from"])
            sender = f"{ sender } -> "
        else:
            sender = ""

        to = encode_bill(item["to"])

        operations_amount = f"{item['operationAmount']['amount']} {item['operationAmount']['currency']['name']}"

        formatted_data.append(f"""\
{date} {description}
{sender}{to}
{operations_amount}""")
    return formatted_data
