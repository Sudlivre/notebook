import csv

from unittest import TestCase
from unittest.mock import Mock

from ddt import ddt, data, unpack


def add(x, y):
    return x + y


# def analyze_data(get_url_data, db):
#     data = get_url_data()
#     items = db.query()
#     # ... ...
#     return True


# def get_url_data_stub():
#     with open('', 'rb') as fs:
#         return fs.read()


@ddt
class TestDbStudent(TestCase):

    def load_data_from_csv(filename):
        data_items = []
        with open(filename, 'r', newline='') as fs:
            reader = csv.reader(fs)
            for row in reader:
                data_items.append(list(map(int, row)))
        return data_items


    @data(*load_data_from_csv('data.csv'))
    @unpack
    def test_add(self, result, param1, param2):
        self.assertEqual(result, add(param1, param2))


    # def test_analyze_data(self):
    #     db = Mock()
    #     db.query.return_value = [11, 121, 12, 144, 255]
    #     self.assertTrue(analyze_data(get_url_data_stub, db))




