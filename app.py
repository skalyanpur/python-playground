from flask import Flask
from flask_jwt import JWT
from flask_restful import Api

from resources.item import Item, ItemList
from resources.user_register import UserRegister
from security import identity, authenticate

app = Flask(__name__)

app.config["PROPAGATE_EXCEPTIONS"] = True
app.secret_key = "flask_jwt"

api = Api(app)

jwt = JWT(app=app, authentication_handler=authenticate, identity_handler=identity)

# api.add_resource(Item, "/item")
api.add_resource(Item, "/item/<string:item_name>")
api.add_resource(ItemList, "/items")
api.add_resource(UserRegister, "/register")

app.run(port=5000, debug=True)
