import pytest
from utils import get_data, get_executed_operations, get_last_operations, get_data_format, encode_bill


def test_get_data():
    data = get_data()
    assert isinstance(data, list)


def test_get_executed_operations(test_data):
    data = get_executed_operations(test_data)
    assert len(data) == 3


def test_get_last_operations(test_data):
    data = get_last_operations(test_data, 3)
    assert [i["date"] for i in data] == ["2020-03-23T10:45:06.972075", "2019-07-03T18:35:29.512364",
                                         "2019-04-04T23:20:05.206878"]


def test_get_data_format(test_data):
    data = get_data_format(test_data)
    assert data == ["26.08.2017 Перевод организации\nMaestro 1596 83** **** 5199 -> Счет **9589\n31957.58 руб.",
                    "03.07.2019 Перевод организации\nMasterCard 7158 30** **** 6758 -> Счет **5560\n8221.37 USD",
                    "30.06.2018 Перевод организации\nСчет **6952 -> Счет **6702\n9824.07 USD",
                    "23.03.2020 Открытие вклада\nСчет **2431\n48223.05 руб.",
                    "04.04.2019 Перевод со счета на счет\nСчет **8542 -> Счет **4188\n79114.93 USD"]


@pytest.mark.parametrize("test_input,expected", [
    ("Счет 64686473678894779589", "Счет **9589"),
    ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199")
])
def test_encode_bill(test_input, expected):
    assert encode_bill(test_input) == expected
