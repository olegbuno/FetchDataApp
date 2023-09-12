import unittest
from run import fetch_data


class TestFetchData(unittest.TestCase):
    def test_empty_field(self):
        records_lst = [{"campaign": "test", "clicks": 1}, {"clicks": 2}, {"campaign": "test2"}]
        result = fetch_data("", records_lst)
        expected_result = "No 'fields' argument passed to fetch"
        self.assertEqual(result, expected_result)

    def test_empty_records(self):
        result = fetch_data("clicks", [])
        expected_result = {'data': []}
        self.assertEqual(result, expected_result)

    def test_fetch_data(self):
        records_lst = [{"campaign": "test", "clicks": 1}, {"clicks": 2}, {"campaign": "test2"}]
        result = fetch_data("clicks", records_lst)
        expected_result = {'data': [{'clicks': 1}, {'clicks': 2}]}
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
