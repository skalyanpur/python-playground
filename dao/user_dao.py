"""
User DAO class
"""
from typing import Optional

from common.base import session_factory
from model.user import User


class UserDao(object):

    @staticmethod
    def create_user(username, password, email_address):
        """

        :param username:
        :param password:
        :param email_address:
        :return:
        """
        try:
            session = session_factory()
            user = User(username=username, password=password, email_address=email_address)
            session.add(user)
            session.commit()
            session.close()
            return user
        except Exception:
            raise

    @staticmethod
    def authenticate_user(username: str, password: str) -> Optional[User]:
        """
        Authenticates user using username and password
        Return at most one result or raise an exception.
        :param username:
        :param password:
        :return:
        """
        session = session_factory()
        # Refer https://docs.sqlalchemy.org/en/14/orm/query.html#sqlalchemy.orm.Query.one_or_none
        user = session.query(User).filter(User.username == username, User.password == password).one_or_none()
        session.close()
        return user

    @staticmethod
    def get_user_by_username(username: str) -> Optional[User]:
        """
        Get User info
        :param username:
        :return:
        """
        session = session_factory()
        user = session.query(User).with_entities(User.username, User.email_address, User.active).filter(
            User.username == username).one_or_none()
        session.close()
        return user

    @staticmethod
    def get_user_by_id(user_id: int) -> Optional[User]:
        """
        
        :param user_id: 
        :return: 
        """

        session = session_factory()
        user = session.query(User).with_entities(User.username, User.email_address, User.active).filter(
            User.id == user_id).one_or_none()
        session.close()
        return user

    def update_user(self, user: User):
        pass

    @staticmethod
    def delete_user(username: str) -> int:
        """

        :param username:
        :return:
        """
        session = session_factory()
        rows_impacted = session.query(User).filter(User.username == username).delete()
        session.commit()
        session.close()

        return rows_impacted


# For debug
# if __name__ == '__main__':
#     UserDao.create_user(username="user1", password="test1", email_address="user1@test.com")
#     UserDao.delete_user(username="user1")
