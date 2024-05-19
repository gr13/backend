import sys
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
    @staticmethod
    def _create_user() -> int:
        """
        Creates a standard user to be used in tests
        """
        random_name = secrets.token_hex(8)
        
        user = UserModel(
            email=f"{random_name}@email.com",
            username="name",
            password="abcd"
        )
        user.save_to_db()
        return user.id

    def test_crud(self):
        """
        Creates model and checks that it was added to db correctly
        """
        with self.app_context():
            # create
            user_id: int = self._create_user()
            # read
            user: UserModel = UserModel.find_by_id(user_id)
            self.assertIsNotNone(user, "Created user is not found")
            # update
            user_name_before = user.username
            user.username = "name2"
            user.save_to_db()
            updated_user: UserModel = UserModel.find_by_id(user_id)
            self.assertNotEqual(
                user_name_before,
                updated_user.username,
                "The user was not updated"
            )
            # delete
            user.delete_from_db()
            self.assertIsNotNone(
                user,
                "User disapered from DB after deletion."
            )
            self.assertTrue(user.hide, "User is not hide after deletion.")
