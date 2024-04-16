# Importing flask module in the project is mandatory 
# An object of Flask class is our WSGI application. 
from flask import Flask,request
from flask_restful import Api
from pymongo import MongoClient
from resources.bill import Bill
from resources.client import Client
from resources.employee import Employee
from resources.menu import Menu

from resources.table import Table

# Flask constructor takes the name of 
# current module (__name__) as argument. 
app = Flask(__name__) 
api = Api(app)

client = MongoClient( 
	'mongodb://localhost:27017/') 

# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function. 
db = client['test'] 
bill = db['bill']
client = db['client']
employee = db['employee']
menu = db['menu']
table = db['table']

api.add_resource(Bill, '/bill', '/bill/<string:id>',resource_class_kwargs={'bill': bill})
api.add_resource(Client, '/client', '/client/<string:id>',resource_class_kwargs={'client': client})
api.add_resource(Employee, '/employee', '/employee/<string:id>',resource_class_kwargs={'employee': employee})
api.add_resource(Menu, '/menu', '/menu/<string:id>',resource_class_kwargs={'menu': menu})
api.add_resource(Table, '/table', '/table/<string:id>',resource_class_kwargs={'table': table, 'bill': bill})
# main driver function 
if __name__ == '__main__':
    app.run(debug=True)
