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

# Run the app
if __name__ == '__main__':
    app.run()

