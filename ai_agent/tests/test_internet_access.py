```python
import unittest
from ai_agent import internet_access

class TestInternetAccess(unittest.TestCase):

    def setUp(self):
        self.internet_access = internet_access.InternetAccess()

    def test_perform_web_search(self):
        search_query = "AI technologies"
        result = self.internet_access.perform_web_search(search_query)
        self.assertIsNotNone(result)

    def test_retrieve_information(self):
        url = "https://www.example.com"
        result = self.internet_access.retrieve_information(url)
        self.assertIsNotNone(result)

    def test_access_external_data_source(self):
        data_source = "https://www.example.com/data.json"
        result = self.internet_access.access_external_data_source(data_source)
        self.assertIsNotNone(result)

    def test_user_permission(self):
        self.assertTrue(self.internet_access.user_permission)

if __name__ == '__main__':
    unittest.main()
```