import json
from dataclasses import asdict
from flask import Flask, request, jsonify
from dao.db_connector import get_db_status
from dao.orm_queries.search_queries import insert_search, get_searches_by_user_id
from dao.orm_queries.city_queries import search_city, insert_city
from dao.orm_queries.result_queries import insert_result
from dao.orm_queries.price_queries import insert_price
from model.search import Search

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
        user_id=request.args.get("user_id")
        search = get_searches_by_user_id(user_id)
        if search is not None:
            result = json.dumps([ob.__dict__ for ob in search], indent=4, sort_keys=True, default=str)
            print(result)
            return json.loads(result), 200
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