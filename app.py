# app.py

from flask import Flask, jsonify, request

app = Flask(__name__)

# Define routes and API endpoints here
@app.route('/hello', methods=['GET'])
def hello_world():
    return jsonify({'message': 'Hello, World!'})

### Define a new route that accepts a name as a parameter
@app.route('/hello/<name>', methods=['GET'])
def hello_name(name):
    return jsonify({'message': 'Hello, ' + name + '!'})

### Define a new route that accepts two numbers as parameters
### Ensure that the parameters are converted to integers
@app.route('/add/<x>/<y>', methods=['GET'])
def add(x, y):
    ### Convert the parameters to integers and handle the ValueError if the conversion fails
    try:
        x = int(x)
        y = int(y)
    except ValueError:
        return jsonify({'message': 'Invalid parameters'}), 400
    return jsonify({'result': x + y})

### Define a new route that accepts two numbers as parameters
### Ensure that the parameters are converted to integers
@app.route('/subtract/<x>/<y>', methods=['GET'])
def subtract(x, y):
    ### Convert the parameters to integers and handle the ValueError if the conversion fails
    try:
        x = int(x)
        y = int(y)
    except ValueError:
        return jsonify({'message': 'Invalid parameters'}), 400
    return jsonify({'result': x - y})

### Write new routes to pass the tests in test_app.py
### Write a new route that accepts two numbers as parameters
### Ensure that the parameters are converted to integers
@app.route('/multiply/<x>/<y>', methods=['GET'])
def multiply(x, y):
    ### Convert the parameters to integers and handle the ValueError if the conversion fails
    try:
        x = int(x)
        y = int(y)
    except ValueError:
        return jsonify({'message': 'Invalid parameters'}), 400
    return jsonify({'result': x * y})

### Write a new route that accepts two numbers as parameters
### Ensure that the parameters are converted to integers
@app.route('/divide/<x>/<y>', methods=['GET'])
def divide(x, y):
    ### Convert the parameters to integers and handle the ValueError if the conversion fails
    try:
        x = int(x)
        y = int(y)
    except ValueError:
        return jsonify({'message': 'Invalid parameters'}), 400
    ### Handle the ZeroDivisionError if the denominator is zero
    try:
        return jsonify({'result': x / y})
    except ZeroDivisionError:
        return jsonify({'message': 'Invalid parameters'}), 400
    
### The root route should return the following: "https://github.com/jcleigh/python-api-ai-assisted"    
@app.route('/', methods=['GET'])
def index():
    return jsonify('https://github.com/jcleigh/python-api-ai-assisted')

# Run the app
if __name__ == '__main__':
    app.run()
