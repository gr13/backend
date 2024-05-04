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
        user = self._create_user()
        expected = {
            "id": None,
            "email":
            "email@email.com",
            "right_id": None,
            "rights": None,
            "username": "name",
            "position": None,
            "can_edit": None,
            "can_seelog": None,
            "can_seeusers": None,
            "hide": None,
        }
        actual: Dict = user.json()
        self.assertEqual(actual, expected,
            f"User JSON is incorrect expected: {expected}, actual: {actual}")
