import logging
from flask_restful import Resource, reqparse
# from werkzeug.security import safe_str_cmp
from src.blacklist import BLACKLIST
from src.models.user import UserModel
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    # jwt_refresh_token_required,
    # get_jwt_identity,
    jwt_required,
    get_jwt,
    # get_jwt_claims
)

_user_parser = reqparse.RequestParser()
_user_parser.add_argument(
    "username",
    type=str,
    required=False,
    help="This field cannot be blanc."
)
_user_parser.add_argument(
    "email",
    type=str,
    required=True,
    help="This field cannot be blanc."
)
_user_parser.add_argument(
    "password",
    type=str,
    required=True,
    help="This field cannot be blank."
)


class UserRegister(Resource):
    @jwt_required()
    def post(self):
        data = _user_parser.parse_args()
        if UserModel.find_by_email(data["email"]):
            logging.info("User with this email is already exists."
                         f" {data['email']}")
            return {"message": "A user with that username already "
                    "exists."}, 400
        user = UserModel(
            email=data["email"],
            username=data["username"],
            password=data["password"]
        )
        user.save_to_db()

        logging.info(f"User {data['email']} created successfully.")
        return {"message": "User created successfully."}, 201


class User(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("email",
                    type=str,
                    required=True,
                    help="This field cannot be empty")
    parser.add_argument("password",
                    type=str,
                    required=False)
    parser.add_argument("right_id",
                    type=int,
                    required=False)
    parser.add_argument("username",
                    type=str,
                    required=False,
                    help="This field cannot be empty")
    parser.add_argument("position",
                    type=str,
                    required=False)

    parser.add_argument("hide",
                    # type=1,
                    choices=["0", "1"],
                    required=False,
                    help="This field accepts only 0 and 1. Error: {error_msg}")

    @classmethod
    @jwt_required()
    def get(cls, user_id):
        user = UserModel.find_by_id(user_id)
        if user:
            return user.json(), 200
        return {"message": "User not found"}, 404

    @classmethod
    @jwt_required()
    def delete(cls, user_id):
        user = UserModel.find_by_id(user_id)
        if user:
            user.delete_from_db()
            return {"message": "User deleted"}, 200

        return {"message": "User not found"}, 404

    @classmethod
    @jwt_required()
    def put(cls, user_id):
        data = User.parser.parse_args()

        item = UserModel.find_by_id(user_id)

        if not item:
            if data["password"]:
                item = UserModel(data["email"], data["password"])
            else:
                return {"message": "User creation requires password."}

        if data["password"] is not None:
            item.set_password(data["password"])
        if data["right_id"] is not None:
            item.right_id = data["right_id"]
        if data["username"] is not None:
            item.username = data["username"]
        if data["hide"] is not None:
            item.hide = int(data["hide"])
        item.save_to_db()

        return item.json()


class UserLogin(Resource):
    @classmethod
    def post(cls):
        data = _user_parser.parse_args()

        user = UserModel.find_by_email(data["email"])

        if user and user.right_id > 1 \
                and user.check_password(data["password"]):
            access_token = create_access_token(identity=user.id, fresh=True)
            refresh_token = create_refresh_token(user.id)
            logging.info(f"User logged in. {data['email']}")
            return {
                "access_token": access_token,
                "refresh_token": refresh_token
            }, 200
        logging.info(f"Invalid credentials. {data['email']}")
        return {"message": "Invalid credentials"}, 401


class UserLogout(Resource):
    @jwt_required()
    def post(self):
        jti = get_jwt()["jti"]
        BLACKLIST.add(jti)
        logging.info("Successfully logged out.")
        return {"message": "Successfully logged out."}, 200


class UserList(Resource):
    @jwt_required()
    def get(self):
        items = UserModel.find_all()
        if items:
            return {"users": [item.json() for item in items]}, 200
        logging.info("Users not found.")
        return {"message": "Users not found."}, 404
