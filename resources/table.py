from flask_restful import Resource
# from app import collection
from flask import request
from schema.table import Table_Schema
from validation.validation import validate_data

import json
from bson import json_util

class Table(Resource):
    def get(self, id = None):
        fillter = {} if id is None else {"number": int(id)}
        list_data = []
        if fillter != {}:
            table = self.table.find_one(fillter)
            return json.loads(json_util.dumps(table))
        for table in self.table.find():
            list_data.append(table) 
        return json.loads(json_util.dumps(list_data))
    def post(self, id = None):
        list_table = []
        for table in self.table.find():
            list_table.append(table['number']) 
        table_data = request.data
        table_data = json.loads(table_data)
        try:
            if self._check_table_existed(table_data['number']):
                return "{} is existed".format(table_data['number'])
            print("Data is valid. Inserting into database...")
            # Insert data into database
        except ValueError as e:
            print(f"Error: {e}")
        table_schema = Table_Schema(number = table_data['number'])
        status = self.table.insert_one({'number': table_data['number']})
        if status != None:
            print(status)
            return "Success"
        return "Failed"
    def put(self, id = None):
        print(Table)
        table_data = request.data
        table_data = json.loads(table_data)
        try:
            if not self._check_table_existed(table_data['number']):
                return "{} is not existed".format(table_data['number'])
            print("Data is valid. Updating into database...")
            # Insert data into database
        except ValueError as e:
            return(f"Error: {e}")
        print('111111111111111 %s',table_data)
        table_instance = Table_Schema(number = table_data['number'])
        print(table_instance)

        # for default_data in table_schema:
        #     if default_data not in table_data:
        #         table_data[default_data] = table_schema[default_data]
        filter = { 'number': int(table_data['number']) }
        status = self.table.update_one(filter, {"$set":table_data}) 
        if status != None:
            return "Success"
        return "Failed"
    def _check_table_existed(self,number_table = None):
        if number_table is None:
            return "Need to provide a number_table "
        list_table = []
        for table in self.table.find():
            list_table.append(table['number']) 
        if number_table in list_table:
            return True
        return False
        