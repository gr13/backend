import os
# import sys
# from pathlib import Path
import logging
from datetime import datetime
from flask import Flask, request, has_request_context
from flask_restful import Api
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv

from src.blacklist import BLACKLIST

from src.resources.user import (
    UserRegister,
    User,
    UserLogin,
    UserLogout,
    UserList
)

load_dotenv()

LOG_FORMAT = "[%(asctime)s] %(levelname)s in %(module)s: %(message)s"
LOG_FILENAME = os.environ["LOG_FILENAME"]
DT_STRING_FORMAT = "%d/%m/%Y %H:%M:%S"

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ["FLASK_SECRET_KEY"]
app.config["DEBUG"] = (os.getenv("DEBUG", "False") == "True")
app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+mysqlconnector://{os.environ['MYSQL_USER']}:{os.environ['MYSQL_ROOT_PASSWORD']}@{os.environ['MYSQL_HOST']}:3306/{os.environ['DATABASE_NAME']}"  # noqa: E501
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["PROPAGATE_EXEPTIONS"] = True
app.config["JWT_BLACKLIST_ENABLED"] = True
app.config["JWT_BLACKLIST_TOKEN_CHECKS"] = ["access", "refresh"]
app.logger.setLevel(logging.DEBUG)  # Set log level to INFO

handler = logging.FileHandler(LOG_FILENAME)  # Log to a file
app.logger.addHandler(handler)

# https://flask.palletsprojects.com/en/2.0.x/logging/

# logging.basicConfig(
#     level=logging.DEBUG,
#     format=log_format
# )


api = Api(app)

jwt = JWTManager(app)


@app.before_request
def log_request_info():
    app.logger.info("######################################################")
    app.logger.info("Request:")
    now = datetime.now()
    app.logger.info(f"datetime: {now.strftime(DT_STRING_FORMAT)}")
    if has_request_context():
        url = request.url
        remote_addr = request.remote_addr
        app.logger.info(f"ip: {remote_addr}, url: {url}")
    if request.headers:
        app.logger.info("Headers: %s", request.headers)
    if request.get_data():
        app.logger.info("Body: %s", request.get_data().decode('ascii'))
    if request.is_json and request.get_json():
        app.logger.info("Json: %s", request.get_json())
    else:
        app.logger.info("No JSON info.")
    app.logger.info("######################################################")


@jwt.token_in_blocklist_loader
def check_if_token_in_blacklist(jwt_header, jwt_payload) -> bool:
    # https://flask-jwt-extended.readthedocs.io/en/stable/blocklist_and_token_revoking/
    return jwt_payload["jti"] in BLACKLIST

# @jwt.user_claims_loader
# def add_claims_to_jwt(identity):
#     user = UserModel.find_by_id(identity)
#     rights = {
#         "right_id": 1,
#         "is_admin": 0,
#         "is_blocked": 1
#     }
#     if user:
#         rights = {
#             "right_id": user.right_id,
#             "is_admin": user.right_id == 7,
#             "is_blocked": user.right_id == 1
#         }

#     return rights


# api.add_resource(Country, '/country/<string:title>')
# api.add_resource(CountryList, '/countries')

# api.add_resource(Region, '/region/<int:region_id>')
# api.add_resource(RegionList, '/regions')


api.add_resource(UserRegister, '/register')
api.add_resource(User, '/user/<int:user_id>')
api.add_resource(UserLogin, '/login')
api.add_resource(UserLogout, '/logout')
api.add_resource(UserList, '/users')


@app.route("/")
def hello():
    app.logger.debug('Hello World!')
    return "Hello World111!"


# sys.stdout = sys.stderr = open('log/flasklog.txt','wt')
