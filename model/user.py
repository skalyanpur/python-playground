from sqlalchemy import Column, String, Boolean, BigInteger

from common.base import Base


class User(Base):
    __tablename__ = 'api_user'

    id = Column(BigInteger, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    active = Column(Boolean, default=True)
    email_address = Column(String, nullable=False)

    def __init__(self, username: str, password: str, email_address: str, _id=None):
        """

        :param username:
        :param password:
        :param email_address:
        """
        self.id = _id
        self.username = username
        self.password = password
        self.email_address = email_address

    # def __str__(self):
    #     return f"Username: {self.username} Email Address: {self.email_address}"
    #
    # def __repr__(self) -> str:
    #     return f"{self.__class__.__name__}({self.username!r}, {self.email_address!r})"
