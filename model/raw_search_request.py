from model.base_model import BaseModel

class RawSearchRequest(BaseModel):

    def __init__(self, args) -> None:
        self.id = args[0]
        self.chat_id = args[1]
        self.request = args[2]
        self.status = args[3]
        self.search_id = args[4]
    
    def __str__(self) -> str:
        return f'id={self.id}, chat_id={self.chat_id}, request = {self.request}, status={self.status}, search_id={self.search_id}'