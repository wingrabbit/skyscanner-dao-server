from orm.base_orm_model import BaseOrmModel
from orm.raw_requests import RawRequests, RawSearchRequest

def insert_raw_request(json_data):
    return RawRequests().insert_values([str(json_data["chat_id"]), str(json_data["request"]), str(json_data["status"])])

def get_new_raw_requests():
    return RawRequests().select_by_field('status', '\'NEW\'', one_record=False)

def update_all_new_searches():
    return RawRequests().update_by_field('status', '\'NEW\'', '\'IN PROGRESS\'')