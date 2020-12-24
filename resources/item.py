from flask_jwt import jwt_required
from flask_restful import Resource, reqparse

from dao.item_dao import ItemDao


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("item_name", type=str, required=True, help="This field cannot be empty")
    parser.add_argument("price", type=float, required=True, help="This field cannot be left blank")

    @jwt_required()
    def get(self, item_name):
        item = ItemDao.get_item(item_name=item_name)
        if item:
            return {"item_name": item.item_name, "price": item.price}
        else:
            return {"message": f"{item_name} not found"}, 404

    @jwt_required()
    def post(self):
        data = Item.parser.parse_args()
        item_name, price = data["item_name"], data["price"]
        item = ItemDao.get_item(item_name=item_name)
        if item:
            return {"message": f"Item with {item_name} already exists"}

        try:
            ItemDao.add_item(item_name=item_name, price=price)
            return {"message": "Item added successfully"}, 201
        except Exception as ex:
            return {"message": "An error occurred inserting an item"}, 401

    def put(self):
        pass

    def delete(self):
        pass


class ItemList(Resource):

    def get(self):
        pass
