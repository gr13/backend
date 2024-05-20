import sys
from typing import Dict
# adding src to the system path
from pathlib import Path
sys.path.append(str(Path(sys.path[0]).parent))
sys.path.append(str(Path(sys.path[0]).parent.parent))
sys.path.append(str(Path(sys.path[0]).parent.parent.parent))
# sys.path.append(str(Path(sys.path[0]).parent.parent.parent.parent))
from src.models.user import UserModel  # noqa:E402
from tests.base_test import BaseTest  # noqa:E402


class UserTest(BaseTest):

    @staticmethod
    def _create_user() -> UserModel:
        """
        Creates a standard user to be used in tests
        """
        return UserModel(
            email="email@email.com",
            username="name",
            password="abcd"
        )

    def test_create_user(self):
        """
        Creates model and checks that email and user name are added correctly
        """
        user = self._create_user()
        self.assertEqual(user.username, "name",
            "The name of the user after creation does not equal"
            " the constructor argument.")
        self.assertEqual(user.email, "email@email.com",
            "The password of the user after creation does not "
            "equal the constructor argument.")

    def test_user_json(self):
        """
        Creates user model and checks the returned json
        """
        with self.app_context():
            user = self._create_user()
            expected = {
                "id": None,
                "email":
                "email@email.com",
                "right_id": 2,
                "right": None,
                "username": "name",
                "can_validate": 0,
                "can_edit": 0,
                "can_seelog": 0,
                "can_seeusers": 0,
                "hide": 0,
                "log_user_id": 0,
                "log_comment": "testing",
            }
            actual: Dict = user.json()
            self.assertDictEqual(actual, expected,
                f"User JSON is incorrect expected: {expected}, actual: "
                    "{actual}")
