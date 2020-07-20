from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required # JSON Web Token

from security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'batman'
api = Api(app)

jwt = JWT(app, authenticate, identity) #returns a JWT token

items = []

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
            type=float,
            required=True,
            help="This field cannot be blank!"
        )
    
    @jwt_required()
    def get(self, name):
        
        # old way 
        # for item in items:
        #     if item['name'] == name:
        #         return item

        item = next(filter(lambda x: x['name'] == name, items), None)
        return {'item': item}, 200 if item else 404

    
    def post(self, name): 
        if next(filter(lambda x: x['name'] == name, items), None):
            return {'message': f"An item with name {name} already exists."}, 400 # 400 = Bad request

        data = Item.parser.parse_args()
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201 # 201 = Resource created

    def delete(self, name):
        global items # <- this tells Python to use the global items for the assignemnt on the next line
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message': f'{name} was deleted'}

     # put is idempotent -> it can be called multiple times but will always give the same result
     # i.e. calling put piano 10 times doesn't create 10 piano objects
    def put(self, name):
        data = Item.parser.parse_args()
        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:
            item = {'name': name, 'price': data['price']}
            items.append(item)
        else:
            item.update(data)
        return item

class ItemList(Resource):
    def get(self):
        return {'items': items}


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

app.run(debug = True)
