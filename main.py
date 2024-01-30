from flask import Flask, request, jsonify
from dao.db_connector import get_db_status
from dao.orm_queries import search_city

app = Flask(__name__)

@app.route("/status")
def home():
    return jsonify(get_db_status()), 200

@app.route("/city")
def city():
    city = search_city(request.args.get("name"))
    if city is not None:
        return jsonify(city.__dict__), 200 
    else: 
        return jsonify({'id': -1}), 404

if __name__ == '__main__':
    app.run(debug=True)