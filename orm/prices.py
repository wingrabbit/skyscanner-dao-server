from orm.base_orm_model import BaseOrmModel
from model.price import Price

class Prices(BaseOrmModel):
    model = Price
    table_name = 'prices'

    default_fields = ['result_id', 'price', 'stops']
    nullable_fields = []