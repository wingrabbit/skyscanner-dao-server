import json
from flask import Flask, request, jsonify
from dao.db_connector import get_db_status
from dao.orm_queries import search_city, insert_city, insert_search

app = Flask(__name__)

@app.route("/status")
def home():
    return jsonify(get_db_status()), 200

@app.route("/city", methods=['GET', 'POST'])
def city():
    if request.method == 'GET':
        city = search_city(request.args.get("name"))
        if city is not None:
            return jsonify(city.__dict__), 200 
        else: 
            return jsonify({'id': -1}), 404
    elif request.method == 'POST':
        data = request.get_json(force=True)
        result = insert_city(data)
        return jsonify(result.__dict__), 200
    
@app.route("/search", methods=['GET', 'POST'])
def search():
    if request.method == 'GET':
        return jsonify({'id': -1}), 404
    elif request.method == 'POST':
        data = request.get_json(force=True)
        result = insert_search(data)
        return jsonify(result.__dict__), 200

if __name__ == '__main__':
    app.run(debug=True)