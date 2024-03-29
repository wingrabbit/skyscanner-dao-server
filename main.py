import json
import logging
from dataclasses import asdict
from flask import Flask, request, jsonify
from dao.db_connector import get_db_status
from dao.orm_queries.search_queries import insert_search, get_searches_by_user_id
from dao.orm_queries.city_queries import search_city, insert_city
from dao.orm_queries.result_queries import insert_result
from dao.orm_queries.price_queries import insert_price
from dao.orm_queries.raw_request_queries import insert_raw_request, get_new_raw_requests, get_raw_requests_by_user_id_and_status, update_search_id_by_id, update_search_status_by_id, get_raw_requests_by_status
from dao.db_connector import select_all_records, select_one_record
from dao.sql_queries.view_queries import get_searches, get_search_by_id, get_top_prices_by_search_id
from model.search import Search

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

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

@app.route("/search/raw", methods=['GET', 'POST'])
def search_raw():
    if request.method == 'POST':
        data = request.get_json(force=True)
        result = insert_raw_request(data)
        return jsonify(result.__dict__), 200
    elif request.method == 'GET':
        raw_requests = get_new_raw_requests()
        if raw_requests is not None:
            result = json.dumps([ob.__dict__ for ob in raw_requests], indent=4, sort_keys=True, default=str)
            #update_all_new_searches()
            return json.loads(result), 200
        return jsonify({'id': -1}), 404

@app.route("/search/raw/<raw_search_id>/update", methods=['GET'])
def search_raw_update(raw_search_id):
    new_status = request.args.get("status")
    search_id = request.args.get("search_id")
    if search_id is not None:
        update_search_id_by_id(raw_search_id, search_id)
    update_search_status_by_id(raw_search_id, new_status)
    return jsonify({'result': 'success'}), 200

@app.route("/searches/user/<user_id>", methods=['GET'])
def search_by_user_id(user_id):
    search = get_searches_by_user_id(user_id)
    if search is not None:
        result = json.dumps([ob.__dict__ for ob in search], indent=4, sort_keys=True, default=str)
        return json.loads(result), 200
    return jsonify({'id': -1}), 404

@app.route("/searches/raw/user/<user_id>", methods=['GET'])
def search_raw_by_user_id(user_id):
    search = get_raw_requests_by_user_id_and_status(user_id, request.args.get("status"))
    if search is not None:
        result = json.dumps([ob.__dict__ for ob in search], indent=4, sort_keys=True, default=str)
        return json.loads(result), 200
    return jsonify({'id': -1}), 404

@app.route("/searches/raw/status/<status>", methods=['GET'])
def search_raw_by_status(status):
    search = get_raw_requests_by_status(status)
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