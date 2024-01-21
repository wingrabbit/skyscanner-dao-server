from dao.db_connector import execute_query, select_one_record
from model.base_model import BaseModel
from model.city import City

class BaseOrmModel:

    model = BaseModel
    table_name=''
    id_field='id'
    default_fields=[]
    nullable_fields=[]

    def model_instance(self, args):
        return globals()[self.model.__name__](args)


    def stringify_list(self, src, escape=False):
        if escape:
            return '\'' + src[0] + '\', \'' + '\', \''.join(src[1:]) + '\''
        return src[0] + ', ' + ', '.join(src[1:])
    
    
    def insert(self, fields: [str], values: [str]):
        """Insert values into correlated fields

        Args:
            fields ([str]): list of fields names
            values([str]): list of correlated values
        Returns:
            str: reslut of the execution
        """
        query = f'INSERT INTO {self.table_name}({self.stringify_list(fields)}) VALUES ({self.stringify_list(values, True)})'
        try:
            execute_query(query)
            return query
        except (Exception) as error:
            return f"Failed to insert: {error}"
    
    
    def insert_values(self, values: [str]):
        """Insert values to the default set of fields

        Args:
            values([str]): list of values to insert
        """
        return self.insert(self.default_fields, values)
    
    
    def select_by_field(self, field, value):
        """Get a matching record"""
        
        query = f'SELECT * FROM {self.table_name} WHERE {field}={value}'
        return self.model_instance(select_one_record(query))