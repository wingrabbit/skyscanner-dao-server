from model.base_model import BaseModel

class Search(BaseModel):
    def __init__(self, args) -> None:
        self.id = args[0]
        self.user_id = args[1]
        self.city_from_id = args[2]
        self.city_to_id = args[3]
        self.date_min = args[4]
        self.date_max = args[5]
        self.days_min = args[6]
        self.days_max = args[7]
    
    def __str__(self) -> str:
        return f'id={self.id}, user_id={self.user_id}, city_from={self.city_from_id}, city_to={self.city_to_id}, date_min={self.date_min}, date_max={self.date_max}, days_min={self.days_min}, days_max={self.days_max}'