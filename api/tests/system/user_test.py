import sys
import json
import secrets
# adding src to the system path
from pathlib import Path
sys.path.append(str(Path(sys.path[0]).parent))
sys.path.append(str(Path(sys.path[0]).parent.parent))
sys.path.append(str(Path(sys.path[0]).parent.parent.parent))
# sys.path.append(str(Path(sys.path[0]).parent.parent.parent.parent))
from src.models.user import UserModel  # noqa:E402
from tests.base_test import BaseTest  # noqa:E402


class UserTest(BaseTest):
    auth_header = None

    def setUp(self):
        """
        Set up the class by logging to the app
        """
        super(UserTest, self).setUp()
        with self.app() as c:
            with self.app_context():
                auth_request = c.post(
                    "/login",
                    data=json.dumps({
                        "email": "admin@gmail.com",
                        "password": "test_password",
                    }),
                    headers={"Content-Type": "application/json"}
                )
                self.assertIn("access_token", json.loads(
                    auth_request.data).keys()
                )
                self.auth_header = "Bearer {}".format(
                    json.loads(auth_request.data)["access_token"])

    def test_register_user_without_login(self):
        """
        Tests user was registered correctly
        """
        with self.app() as c:
            with self.app_context():
                random_email = f"{secrets.token_hex(8)}@email.com"
                user_data = {
                    "email": random_email,
                    "username": "name",
                    "password": "abcd"
                }
                r = c.post(
                    "/register",
                    data=user_data
                )
                self.assertEqual(r.status_code, 401)
                self.assertIsNone(UserModel.find_by_email(random_email))
                self.assertDictEqual(
                    d1={"msg": "Missing Authorization Header"},
                    d2=json.loads(r.data)
                )

    def test_wrong_login(self):
        """
        Tests user was registered correctly
        """
        with self.app() as c:
            with self.app_context():
                auth_request = c.post(
                    "/login",
                    data=json.dumps({
                        "email": "test@test.com",
                        "password": "test",
                    }),
                    headers={"Content-Type": "application/json"}
                )
                self.assertNotIn("access_token", json.loads(
                    auth_request.data).keys()
                )

    def test_register_user(self):
        """
        Tests user was registered correctly
        """
        with self.app() as c:
            with self.app_context():
                random_email = f"{secrets.token_hex(8)}@email.com"
                user_data = {
                    "email": random_email,
                    "username": "name",
                    "password": "abcd",
                }
                r = c.post(
                    "/register",
                    data=json.dumps(user_data),
                    headers={
                        "Authorization": self.auth_header,
                        "Content-Type": "application/json",
                    }
                )
                self.assertEqual(r.status_code, 201)
                self.assertIsNotNone(UserModel.find_by_email(random_email))
                self.assertDictEqual(
                    d1={"message": "User created successfully."},
                    d2=json.loads(r.data)
                )

    def test_get_user(self):
        """
        Tests user was get correctly
        """
        with self.app() as c:
            with self.app_context():
                r = c.get(
                    "/user/1",
                    headers={
                        "Authorization": self.auth_header,
                    }
                )
                expected = {
                    "id": 1,
                    "email": "blocked@email.com",
                    "right_id": 1,
                    "right": {"id": 1, "right": "blocked"},
                    "username": "blocked",
                    "can_validate": False,
                    "can_edit": False,
                    "can_seelog": False,
                    "can_seeusers": False,
                    "hide": False,
                    "log_user_id": 0,
                    "log_comment": None
                }

                self.assertEqual(r.status_code, 200)
                self.assertDictEqual(
                    d1=expected,
                    d2=json.loads(r.data)
                )

    def test_delete_user(self):
        """
        Tests user was deleted correctly
        """
        with self.app() as c:
            with self.app_context():
                # create user
                random_email = f"{secrets.token_hex(8)}@email.com"
                user_data = {
                    "email": random_email,
                    "username": "name",
                    "password": "abcd",
                }
                r = c.post(
                    "/register",
                    data=json.dumps(user_data),
                    headers={
                        "Authorization": self.auth_header,
                        "Content-Type": "application/json",
                    }
                )
                self.assertEqual(r.status_code, 201)
                new_user: UserModel = UserModel.find_by_email(random_email)
                self.assertIsNotNone(new_user)
                self.assertDictEqual(
                    d1={"message": "User created successfully."},
                    d2=json.loads(r.data)
                )
                # delete user
                r = c.delete(
                    f"/user/{new_user.id}",
                    headers={
                        "Authorization": self.auth_header,
                    }
                )
                expected = {"message": "User deleted"}

                self.assertEqual(r.status_code, 200)
                self.assertDictEqual(
                    d1=expected,
                    d2=json.loads(r.data)
                )

                # check that user was delete correctly (hided)
                self.assertTrue(new_user.hide)

    def test_put_user_username_update(self):
        """
        Tests user was put correctly
        """
        with self.app() as c:
            with self.app_context():
                # create user
                random_email = f"{secrets.token_hex(8)}@email.com"
                user_data = {
                    "email": random_email,
                    "username": "name",
                    "password": "abcd",
                }
                r = c.post(
                    "/register",
                    data=json.dumps(user_data),
                    headers={
                        "Authorization": self.auth_header,
                        "Content-Type": "application/json",
                    }
                )
                self.assertEqual(r.status_code, 201)
                new_user: UserModel = UserModel.find_by_email(random_email)
                self.assertIsNotNone(new_user)
                self.assertDictEqual(
                    d1={"message": "User created successfully."},
                    d2=json.loads(r.data)
                )
                self.assertEqual(new_user.username, "name")
                # put user
                user_data = {
                    "email": random_email,
                    "username": "name2"
                }
                r = c.put(
                    f"/user/{new_user.id}",
                    data=json.dumps(user_data),
                    headers={
                        "Authorization": self.auth_header,
                        "Content-Type": "application/json",
                    }
                )
                self.assertEqual(r.status_code, 200)

                # check that username was updated
                self.assertEqual(new_user.username, "name2")
