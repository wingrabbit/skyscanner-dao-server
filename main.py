from flask import Flask, request, jsonify
from dao.db_connector import get_db_status

app = Flask(__name__)

@app.route("/status")
def home():
    return jsonify(get_db_status()), 200

if __name__ == '__main__':
    app.run(debug=True)