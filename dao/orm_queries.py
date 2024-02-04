from dao.db_connector import execute_query, select_one_record

from orm.base_orm_model import BaseOrmModel
from orm.cities import Cities, City
from orm.searches import Searches, Search

def search_city(city_name):
    return Cities().select_by_field_ilike('name', f'\'{city_name}\'')

def insert_city(json_data):
    return Cities().insert_values([str(json_data["name"]), str(json_data["sky_id"]), str(json_data["entity_id"])])

def insert_search(json_data):
    return Searches().insert_values([str(json_data["user_id"]),str(json_data["city_from_id"]),str(json_data["city_to_id"]),str(json_data["date_min"]),str(json_data["date_max"]),str(json_data["days_min"]),str(json_data["days_max"])])