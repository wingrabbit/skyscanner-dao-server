from dao.db_connector import execute_query, select_one_record
from model.base_model import BaseModel
from model.city import City
from model.result import Result
from model.price import Price
from model.search import Search

class BaseOrmModel:

    model = BaseModel
    repetitive = False
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
            values ([str]): list of correlated values
        Returns:
            (Model): instance of the related models with the inserted values
        """
        if not self.repetitive:
            attempt = self.select_by_multiple_fields(fields, values)
            if attempt is not None:
                return attempt

        query = f'INSERT INTO {self.table_name}({self.stringify_list(fields)}) VALUES ({self.stringify_list(values, True)})'
        try:
            execute_query(query)
        except (Exception) as error:
            return f"Failed to insert: {error}"
        return self.select_by_multiple_fields(fields, values)
    
    
    def insert_values(self, values: [str]):
        """Insert values to the default set of fields

        Args:
            values([str]): list of values to insert
        """
        return self.insert(self.default_fields, values)
    
    
    def select_by_field(self, field, value):
        """Get a matching record by the value of the field
        
        Args:
            field (str): field to compare
            value (str): value to check
        Returns:
            (Model): instance of related model or None
        """
        
        query = f'SELECT * FROM {self.table_name} WHERE {field}={value}'
        record = select_one_record(query)
        if record is not None:
            return self.model_instance(select_one_record(query))
        return None
    

    def select_by_multiple_fields(self, fields, values):
        """Get a matching record by values of multiple fields
        
        Args:
            fields ([str]): fields to compare
            values ([str]): values to check
        Returns:
            (Model): instance of related model if exists or None
        """
        
        query = f'SELECT * FROM {self.table_name} WHERE '
        for field, value in zip(fields, values):
            val = value
            if not isinstance(value, int) or isinstance(value, float):
                val = f'\'{value}\''
            query += f'{field}={val} AND '
        query = query.removesuffix(' AND ')
        record = select_one_record(query)
        if record is not None:
            return self.model_instance(select_one_record(query))
        return None
    
    def select_by_field_ilike(self, field, value):
        """Get a matching record by the value of the field
        
        Args:
            field (str): field to compare
            value (str): value to check
        Returns:
            (Model): instance of related model or None
        """
        
        query = f'SELECT * FROM {self.table_name} WHERE {field} ILIKE {value}'
        record = select_one_record(query)
        if record is not None:
            return self.model_instance(select_one_record(query))
        return None