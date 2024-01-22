from model.base_model import BaseModel

class Price(BaseModel):
    def __init__(self, args) -> None:
        self.id = args[0]
        self.result_id = args[1]
        self.price = args[2]
        self.stops = args[3]
    
    def __str__(self) -> str:
        return f'id={self.id}, result_id={self.result_id}, ${self.price}, {self.stops} stops'