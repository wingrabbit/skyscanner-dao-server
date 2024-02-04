import json
from flask import Flask, request, jsonify
from dao.db_connector import get_db_status
from dao.orm_queries.search_queries import insert_search
from dao.orm_queries.city_queries import search_city, insert_city
from dao.orm_queries.result_queries import insert_result
from dao.orm_queries.price_queries import insert_price

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
    
@app.route("/result", methods=['GET', 'POST'])
def result():
    if request.method == 'GET':
        return jsonify({'id': -1}), 404
    elif request.method == 'POST':
        data = request.get_json(force=True)
        result = insert_result(data)
        return jsonify(result.__dict__), 200

@app.route("/price", methods=['GET', 'POST'])
def price():
    if request.method == 'GET':
        return jsonify({'id': -1}), 404
    elif request.method == 'POST':
        data = request.get_json(force=True)
        result = insert_price(data)
        return jsonify(result.__dict__), 200

if __name__ == '__main__':
    app.run(debug=True)