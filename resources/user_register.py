from flask_restful import Resource, reqparse

from dao.user_dao import UserDao


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("username", type=str, required=True, help="This field cannot be blank")
    parser.add_argument("password", type=str, required=True, help="This field cannot be blank")
    parser.add_argument("email_address", type=str, required=True, help="This field cannot be blank")

    def post(self):
        """
        Create user in `api_user` table
        :return:
        """
        try:
            data = UserRegister.parser.parse_args()
            username, password, email_address = data["username"], data["password"], data["email_address"]
            user = UserDao.get_user_by_username(username=username)
            if user:
                return {"message": "User with that username already exists"}, 400

            UserDao.create_user(username=username, password=password, email_address=email_address)
            return {"message": "User created successfully"}, 201

        except Exception as exception:
            return {
                       "message": "Internal error occurred",
                       "error": str(exception)
                   }, 500
