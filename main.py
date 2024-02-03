import json
from flask import Flask, request, jsonify
from dao.db_connector import get_db_status
from dao.orm_queries import search_city

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
        json_response = json.loads(data)
        return json_response

if __name__ == '__main__':
    app.run(debug=True)