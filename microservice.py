from flask import Flask, request, jsonify
import random

app = Flask(__name__)


@app.route('/generate', methods=['POST'])
def generate_random_number():
    data = request.get_json()

    try:
        max_val = int(data.get('max', 0)) # If 'max' is not provided, 0 will be used
    except ValueError:
        return jsonify({'error': "Invalid 'max' value. It must be an integer."}), 400

    if max_val < 0:
        return jsonify({'error': "Invalid 'max' value. It must be non-negative."}), 400

    random_number = random.randint(0, max_val)

    return jsonify({'random_number': random_number})

if __name__ == '__main__':
    app.run(port=5000)