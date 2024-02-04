from orm.base_orm_model import BaseOrmModel
from orm.results import Results, Result

def insert_result(json_data):
    return Results().insert_values([str(json_data["search_id"]), str(json_data["date_from"]), str(json_data["date_return"])])