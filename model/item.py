from sqlalchemy import Column, BigInteger, Float, String

from common.base import Base


class Item(Base):
    __tablename__ = "item"

    id = Column(BigInteger, primary_key=True)
    item_name = Column(String, nullable=False)
    price = Column(Float, nullable=False)

    def __init__(self, name, price):
        self.id = None
        self.item_name = name
        self.price = price

    # def __repr__(self):
    #     return f"{self.__class__.item_name}({self.item_name!r}, {self.price!r})"
    #
    # def __str__(self):
    #     return f"Product name: {self.item_name}, Price: {self.price}"
