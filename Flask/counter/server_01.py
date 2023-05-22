from flask import Flask, jsonify, request
from counting import counting

app = Flask(__name__)
locations = ['Tampere', 'Helsinki']


# Example route
@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify(message='Hello, world!')

# Example route with query parameter
@app.route('/api/greet', methods=['GET'])
def greet():
    name = request.args.get('name')
    if name:
        counting()
        return jsonify(message=f'Hello, {name}! here are the locations {locations}')

    else:
        return jsonify(message='Hello, there!')

if __name__ == '__main__':
    app.run(debug=True)
