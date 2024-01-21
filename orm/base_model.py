class BaseModel:

    table_name=''

    def stringify_list(self, src):
        return src[0] + ', ' + ', '.join(src[1:])
    
    def insert(self, fields: [str], values: [str]):
        query = f'INSERT INTO {self.table_name}({self.stringify_list(fields)}) VALUES ({self.stringify_list(values)})'
        return query