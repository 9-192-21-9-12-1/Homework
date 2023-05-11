import pytest
from utils import get_last_values, get_formatted_data, get_filtered_data, get_data


def test_get_data():
    data = get_data()
    assert isinstance(data, list)
    assert len(data) > 0

def test_get_filtered_data(test_data):
    assert get_filtered_data(test_data[:2]) ==[{
        'date': '2019-07-03Т18:35:29.512364',
        'description': 'Перевод организации',
        'id': 41428829,
        'operationAmount':{
            'amount': '8221.37',
            'currency':{
                'code': 'USD',
                'name': 'USD'
            }
        },
        'state': 'EXECUTED',
        'to':'Счет 35383033474447895560'
    }]
    assert get_filtered_data(test_data[:2], filter_empty_from=True) ==[]


def test_get_last_values(test_data):
    data = get_last_values(test_data, 4)
    assert [x["date"] for x in data] == ['2019-08-26T10:50:58.294041', '2019-07-03T18:35:29.512364', '2019-04-04T23:20:05.206878', '2019-03-23T01:09:46.296404']
def test_get_formatted_data(test_data):
    data = get_formatted_data(test_data)
    expected = ['26.08.19 Перевод организации\nMaestro 1596 83** **** 5199 -> Счет **9589\n31957.58 руб.','03.07.19 Перевод организации\nMaestro 1596 83** **** 5199 -> Счет **5560\n8221.37 USD','30.06.18 Перевод организации\nСчет **6952 -> Счет **6702\n9824.07 USD','04.04.19 Перевод со счета на счет\nСчет **8542 -> Счет **4188\n79114.93 USD','23.03.19 Перевод со счета на счет\nСчет 4481 22 **** 4719 -> Счет **1160\n43318.34 руб.']
    assert data == expected






