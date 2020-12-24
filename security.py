from dao.user_dao import UserDao


def authenticate(username, password):
    """
    Authentication handler called by JWT
    :param username:
    :param password:
    :return:
    """
    user = UserDao.authenticate_user(username=username, password=password)
    return user


def identity(payload):
    """
    Identity handler called by JWT
    :param payload:
    :return:
    """
    user_id = payload["identity"]
    return UserDao.get_user_by_id(user_id=user_id)
