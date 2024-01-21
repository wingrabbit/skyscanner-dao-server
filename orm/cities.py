from orm.base_model import BaseModel

class Cities(BaseModel):
    
    table_name = 'cities'

    default_fields = ['name', 'sky_id', 'entity_id']
    nullable_fields = ['country_id']