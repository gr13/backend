"""
BaseTest
This class should be parent to each test.
It allows for instantiation of the database dynamically,
and make sure that it is a new, blank database each time.
"""
import os
import sys
from unittest import TestCase

# adding src to the system path
from pathlib import Path
sys.path.append(str(Path(sys.path[0]).parent))
from dotenv import load_dotenv  # noqa:E402
load_dotenv()
os.environ["LOG_FILENAME"] = "api.log"

from src import app  # noqa:E402
from src.db import db  # noqa:E402


class BaseTest(TestCase):
    # SQLALCHEMY_DATABASE_URI = "sqlite:///data_test.db"
    SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{os.environ['MYSQL_USER']}:{os.environ['MYSQL_ROOT_PASSWORD']}@{os.environ['MYSQL_HOST']}:3306/{os.environ['DATABASE_NAME']}"  # noqa: E501

    @classmethod
    def setUpClass(cls):
        app.config["SQLALCHEMY_DATABASE_URI"] = BaseTest.SQLALCHEMY_DATABASE_URI  # noqa: E501
        app.config["DEBUG"] = True
        with app.app_context():
            db.init_app(app)
            # create_db(os.environ["TEST_DATABASE_NAME"])

    def setUp(self):
        with app.app_context():
            # SHOW DATABASES;
            db.create_all()
        self.app = app.test_client
        self.app_context = app.app_context

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()
