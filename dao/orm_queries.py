from dao.db_connector import execute_query, select_one_record

from orm.base_orm_model import BaseOrmModel
from orm.cities import Cities, City
from orm.searches import Searches, Search
from orm.results import Results, Result
from orm.prices import Prices, Price

def search_city(city_name):
    return Cities().select_by_field_ilike('name', f'\'{city_name}\'')

def insert_city(json_data):
    return Cities().insert_values([str(json_data["name"]), str(json_data["sky_id"]), str(json_data["entity_id"])])

def insert_search(json_data):
    return Searches().insert_values([str(json_data["user_id"]),str(json_data["city_from_id"]),str(json_data["city_to_id"]),str(json_data["date_min"]),str(json_data["date_max"]),str(json_data["days_min"]),str(json_data["days_max"])])

def insert_result(json_data):
    return Results().insert_values([str(json_data["search_id"]), str(json_data["date_from"]), str(json_data["date_return"])])

def insert_price(json_data):
    return Prices().insert_values([str(json_data["result_id"]), str(json_data["price"]), str(json_data["stops"])])