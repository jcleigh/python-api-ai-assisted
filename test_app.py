# test_app.py

import unittest
from app import app

class TestAPI(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_hello_world(self):
        response = self.app.get('/hello')
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], 'Hello, World!')

### Write a test for a new endpoint /hello/<name> that returns a JSON object with a message containing the name passed in the URL. For example, /hello/John should return {"message": "Hello, John!"}.       
    def test_hello_name(self):
        response = self.app.get('/hello/John')
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], 'Hello, John!')

if __name__ == '__main__':
    unittest.main()
