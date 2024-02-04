from orm.base_orm_model import BaseOrmModel
from orm.prices import Prices, Price

def insert_price(json_data):
    return Prices().insert_values([str(json_data["result_id"]), str(json_data["price"]), str(json_data["stops"])])