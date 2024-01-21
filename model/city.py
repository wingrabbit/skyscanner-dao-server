from model.base_model import BaseModel

class City(BaseModel):
    def __init__(self, args) -> None:
        self.id = args[0]
        self.name = args[1]
        self.country_id = args[2]
        self.sky_id = args[3]
        self.entity_id = args[4]
    
    def __str__(self) -> str:
        return f'id={self.id}, name={self.name}, country_id={self.country_id}, sky_id={self.sky_id}, entity_id={self.entity_id}'