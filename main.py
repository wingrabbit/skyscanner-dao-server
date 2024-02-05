import json
from dataclasses import asdict
from flask import Flask, request, jsonify
from dao.db_connector import get_db_status
from dao.orm_queries.search_queries import insert_search, get_searches_by_user_id
from dao.orm_queries.city_queries import search_city, insert_city
from dao.orm_queries.result_queries import insert_result
from dao.orm_queries.price_queries import insert_price
from dao.db_connector import select_all_records, select_one_record
from dao.sql_queries.view_queries import get_searches, get_search_by_id, get_top_prices_by_search_id
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
    data = request.get_json(force=True)
    result = insert_search(data)
    return jsonify(result.__dict__), 200

@app.route("/searches/user/<user_id>", methods=['GET'])
def search_by_user_id(user_id):
    search = get_searches_by_user_id(user_id)
    if search is not None:
        result = json.dumps([ob.__dict__ for ob in search], indent=4, sort_keys=True, default=str)
        return json.loads(result), 200
    return jsonify({'id': -1}), 404

@app.route("/searches/<search_id>", methods=['GET'])
def search_by_id(search_id):
    search = select_one_record(get_search_by_id(search_id))
    if search is not None:
        result = json.dumps(search, indent=4, sort_keys=True, default=str)
        return json.loads(result), 200
    return jsonify({'id': -1}), 404

@app.route("/searches/<search_id>/prices", methods=['GET'])
def prices_by_search_id(search_id):
    limit = request.args.get("limit")
    search = select_all_records(get_top_prices_by_search_id(search_id)) if limit is None else select_all_records(get_top_prices_by_search_id(search_id, limit))
    if search is not None:
        result = json.dumps([ob for ob in search], indent=4, sort_keys=True, default=str)
        return json.loads(result), 200
    return jsonify({'id': -1}), 404
    
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