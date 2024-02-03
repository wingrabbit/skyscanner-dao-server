from model.base_model import BaseModel

class Result(BaseModel):
    def __init__(self, args) -> None:
        self.id = args[0]
        self.search_id = args[1]
        self.date_from = args[2]
        self.date_return = args[3]
        self.last_updated = args[4]
    
    def __str__(self) -> str:
        return f'id={self.id}, search={self.search_id} {self.date_from}-{self.date_return}, updated {self.last_updated}'