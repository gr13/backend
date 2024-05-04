import sys
# adding src to the system path
from pathlib import Path
sys.path.append(str(Path(sys.path[0]).parent))
sys.path.append(str(Path(sys.path[0]).parent.parent))
sys.path.append(str(Path(sys.path[0]).parent.parent.parent))
# sys.path.append(str(Path(sys.path[0]).parent.parent.parent.parent))
from src.models.user import UserModel  # noqa:E402
from tests.base_test import BaseTest  # noqa:E402


class UserTest(BaseTest):
    def test_create_user(self):
        user = UserModel(
            "email@email.com", "name", "abcd"
        )

        self.assertEqual(user.username, "name",
                        "The name of the user after creation does not equal"  # noqa E128
                        " the constructor argument.")  # noqa E128
        self.assertEqual(user.email, "email@email.com",
                        "The password of the user after creation does not "  # noqa E128
                        "equal the constructor argument.")  # noqa E128
