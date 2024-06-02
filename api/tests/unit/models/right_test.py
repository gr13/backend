import sys
from typing import Dict
# adding src to the system path
from pathlib import Path
sys.path.append(str(Path(sys.path[0]).parent))
sys.path.append(str(Path(sys.path[0]).parent.parent))
sys.path.append(str(Path(sys.path[0]).parent.parent.parent))
from src.models.user_right import UserRightModel  # noqa:E402
from tests.base_test import BaseTest  # noqa:E402


class UserRightTest(BaseTest):

    def test_user_right_json(self):
        """
        Creates user model and checks the returned json
        """
        with self.app_context():
            right = UserRightModel.find_by_id(2)
            expected = {
                "id": 2,
                "right": "player"
            }
            actual: Dict = right.json()
            self.assertDictEqual(actual, expected,
                f"User JSON is incorrect expected: {expected}, actual: "
                    "{actual}")

    def test_user_right_users(self):
        """
        Creates user model and checks the returned json
        """
        with self.app_context():
            right = UserRightModel.find_by_id(2)
            expected = {
                'id': 2,
                'email': 'player@email.com',
                'right_id': 2,
                'right': {'id': 2, 'right': 'player'},
                'username': 'player',
                'can_validate': False,
                'can_edit': False,
                'can_seelog': False,
                'can_seeusers': False,
                'hide': False,
                'log_user_id': 0,
                'log_comment': None
            }

            actual: Dict = right.get_users_json()
            self.assertTrue(
                actual.get("users"),
                "users field is missing in get_users_json response"
            )
            self.assertDictEqual(actual["users"][0], expected,
                f"User JSON is incorrect expected: {expected}, actual: "
                    f"{actual}")
