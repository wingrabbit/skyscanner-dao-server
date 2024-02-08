from orm.base_orm_model import BaseOrmModel
from model.raw_search_request import RawSearchRequest

class RawRequests(BaseOrmModel):
    
    model = RawSearchRequest
    table_name = 'raw_requests'

    default_fields = ['chat_id', 'request', 'status']
    nullable_fields = ['search_id']