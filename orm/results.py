from orm.base_orm_model import BaseOrmModel
from model.result import Result

class Results(BaseOrmModel):
    
    model = Result
    table_name = 'results'

    default_fields = ['city_from_id', 'city_to_id', 'date_from', 'date_return']
    nullable_fields = ['last_updated']