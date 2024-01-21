class BaseModel:

    table_name=''
    id_field='id'
    default_fields=[]
    nullable_fields=[]

    def stringify_list(self, src):
        return src[0] + ', ' + ', '.join(src[1:])
    
    def insert(self, fields: [str], values: [str]):
        """Insert values into correlated fields

        Args:
            fields ([str]): list of fields names
            values([str]): list of correlated values
        Returns:
            str: reslut of the execution
        """
        query = f'INSERT INTO {self.table_name}({self.stringify_list(fields)}) VALUES ({self.stringify_list(values)})'
        return query
    
    def insert_values(self, values):
        """Insert values to the default set of fields"""
        return self.insert(self.default_fields, values)