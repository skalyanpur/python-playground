# NOTE: OlD WAY OF DOING THIS
# from flask import Flask, jsonify, request
#
# app = Flask(__name__)
#
# stores = [
#     {
#         "name": "Store1",
#         "items":
#             [
#                 {
#                     "name": "item1",
#                     "price": 15.99
#                 },
#                 {
#                     "name": "item2",
#                     "price": 16.99
#                 }
#             ]
#     },
#     {
#         "name": "Store2",
#         "items":
#             [
#                 {
#                     "name": "item3",
#                     "price": 15.99
#                 },
#                 {
#                     "name": "item4",
#                     "price": 16.99
#                 }
#             ]
#     }
# ]
#
#
# @app.route("/")
# def home():
#     return "Hello, world!"
#
#
# @app.route("/store", methods=["POST"])
# def create_store():
#     request_data = request.get_json()
#     new_store = {
#         "name": request_data["name"],
#         "items": []
#     }
#     stores.append(new_store)
#     return jsonify(new_store)
#
#
# @app.route("/store/<string:name>")
# def get_store(name):
#     for store in stores:
#         if name.lower() == store["name"].lower():
#             return jsonify(store)
#
#     return {"message": "Store not found"}
#
#
# @app.route("/store")
# def get_stores():
#     return jsonify({"stores": [store["name"] for store in stores]})
#
#
# @app.route("/store/<string:name>/item", methods=["POST"])
# def create_item_in_store(name):
#     request_data = request.get_json()
#     for store in stores:
#         if name.lower() == store["name"].lower():
#             new_item = {
#                 "name": request_data["name"],
#                 "price": request_data["price"]
#             }
#             store.get("items", []).append(new_item)
#             return jsonify(new_item)
#     return jsonify({"message": "Store not found"})
#
#
# app.run(port=5000)
