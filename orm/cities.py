from orm.base_orm_model import BaseOrmModel

class Cities(BaseOrmModel):
    
    table_name = 'cities'

    default_fields = ['name', 'sky_id', 'entity_id']
    nullable_fields = ['country_id']