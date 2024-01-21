from orm.base_orm_model import BaseOrmModel
from model.city import City

class Cities(BaseOrmModel):
    
    model = City
    table_name = 'cities'

    default_fields = ['name', 'sky_id', 'entity_id']
    nullable_fields = ['country_id']