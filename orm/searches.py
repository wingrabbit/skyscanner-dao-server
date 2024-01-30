from orm.base_orm_model import BaseOrmModel
from model.search import Search

class Searches(BaseOrmModel):

    model = Search
    table_name = 'searches'

    default_fields = ['user_id', 'city_from_id', 'city_to_id', 'date_min', 'date_max', 'days_min', 'days_max']