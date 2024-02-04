from dao.db_connector import execute_query, select_one_record

from orm.base_orm_model import BaseOrmModel
from orm.searches import Searches, Search

def insert_search(json_data):
    return Searches().insert_values([str(json_data["user_id"]),str(json_data["city_from_id"]),str(json_data["city_to_id"]),str(json_data["date_min"]),str(json_data["date_max"]),str(json_data["days_min"]),str(json_data["days_max"])])

def get_searches_by_user_id(user_id):
    return Searches().select_by_field('user_id', f'\'{user_id}\'', one_record=False)