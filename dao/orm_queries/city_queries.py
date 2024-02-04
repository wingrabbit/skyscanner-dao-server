from orm.base_orm_model import BaseOrmModel
from orm.cities import Cities, City

def search_city(city_name):
    return Cities().select_by_field_ilike('name', f'\'{city_name}\'')

def insert_city(json_data):
    return Cities().insert_values([str(json_data["name"]), str(json_data["sky_id"]), str(json_data["entity_id"])])