from orm.base_orm_model import BaseOrmModel
from orm.raw_requests import RawRequests, RawSearchRequest

def insert_raw_request(json_data):
    return RawRequests().insert_values([str(json_data["chat_id"]), str(json_data["request"]), str(json_data["status"])])