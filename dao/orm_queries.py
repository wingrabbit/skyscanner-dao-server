from dao.db_connector import execute_query, select_one_record

from orm.base_orm_model import BaseOrmModel
from orm.cities import Cities, City

def search_city(city_name):
    return Cities().select_by_field_ilike('name', f'\'{city_name}\'')