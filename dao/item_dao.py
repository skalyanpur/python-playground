from common.base import session_factory
from model.item import Item


class ItemDao(object):
    def __init__(self):
        pass

    @staticmethod
    def get_item(item_name):
        session = session_factory()
        item = session.query(Item).filter(Item.item_name == item_name).one_or_none()
        session.close()
        return item

    @staticmethod
    def add_item(item_name, price):
        item = Item(name=item_name, price=price)
        session = session_factory()
        session.add(item)
        session.commit()
        session.close()
