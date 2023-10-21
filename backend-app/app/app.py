from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/data')
def get_data():
    data = {
        "example": "API is working"
    }
    return jsonify(data)


