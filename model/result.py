from model.base_model import BaseModel

class Result(BaseModel):
    def __init__(self, args) -> None:
        self.id = args[0]
        self.city_from_id = args[1]
        self.city_to_id = args[2]
        self.date_from = args[3]
        self.date_return = args[4]
        self.last_updated = args[5]
    
    def __str__(self) -> str:
        return f'id={self.id}, {self.city_from_id}-{self.city_from_id} {self.date_from}-{self.date_return}, updated {self.last_updated}'