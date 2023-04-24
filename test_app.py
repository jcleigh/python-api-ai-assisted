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

### Write a test for a new endpoint /add/x/y that performs addition on the two numbers x and y and returns a JSON object with the result. For example, /add/1/2 should return {"result": 3}.
    def test_add1(self):
        response = self.app.get('/add/1/2')
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['result'], 3)   

### Write a test for the /add/x/y endpoint that checks that the result is an integer. For example, /add/1/2 should return {"result": 3} and /add/1.5/2.5 should return {"result": 4}.
    def test_add2(self):
        response = self.app.get('/add/1/2')
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        
### Write a test for the /add/x/y endpoint that tests the error handling for invalid parameters. For example, /add/1/abc should return {"message": "Invalid parameters"} and a status code of 400.
    def test_add3(self):
        response = self.app.get('/add/1/abc')
        data = response.get_json()
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['message'], 'Invalid parameters')

### Duplicate the /add/x/y tests for a new endpoint that performs subtraction.
    def test_sub1(self):
        response = self.app.get('/subtract/1/2')
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['result'], -1)
        
### Now test the error handling for invalid parameters for the subtraction endpoint.
    def test_sub2(self):
        response = self.app.get('/subtract/1/abc')
        data = response.get_json()
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['message'], 'Invalid parameters')

### Duplicate the /add/x/y tests for a new endpoint that performs multiplication.
    def test_mul1(self):
        response = self.app.get('/multiply/1/2')
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['result'], 2)

### Now test the error handling for invalid parameters for the multiplication endpoint.
    def test_mul2(self):
        response = self.app.get('/multiply/1/abc')
        data = response.get_json()
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['message'], 'Invalid parameters')

### Now write tests for a new endpoint that performs division.
    def test_div1(self):
        response = self.app.get('/divide/1/2')
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['result'], 0.5)

### Now test the error handling for invalid parameters for the division endpoint.
    def test_div2(self):
        response = self.app.get('/divide/1/abc')
        data = response.get_json()
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['message'], 'Invalid parameters')
    
if __name__ == '__main__':
    unittest.main()
