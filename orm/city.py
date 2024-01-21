from orm.base_model import BaseModel

class City(BaseModel):
    
    table_name = 'cities'

    default_fields = ['name', 'sky_id', 'entity_id']
    nullable_fields = ['country_id']

    def __init__(self, name, sky_id, entity_id):
        self.name = name
        self.sky_id = sky_id
        self.entity_id = entity_id