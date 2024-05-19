import sys

# adding src to the system path
from pathlib import Path
sys.path.append(str(Path(sys.path[0]).parent))
sys.path.append(str(Path(sys.path[0]).parent.parent))
sys.path.append(str(Path(sys.path[0]).parent.parent.parent))
# sys.path.append(str(Path(sys.path[0]).parent.parent.parent.parent))
from src.models.game import GameModel  # noqa:E402
from tests.base_test import BaseTest  # noqa:E402


class UserTest(BaseTest):
    @staticmethod
    def _create_game() -> int:
        """
        Creates a game to be used in tests
        """

        game = GameModel(
            user_id=1,
            game_description="game_description"
        )
        game.save_to_db()
        return game.id

    def test_crud(self):
        """
        Creates model and checks that it was added to db correctly
        """
        with self.app_context():
            # create
            game_id: int = self._create_game()
            # read
            game: GameModel = GameModel.find_by_id(game_id)
            self.assertIsNotNone(game, "Created user is not found")
            # update
            game_description_before = game.game_description
            game.game_description = "game_description2"
            game.save_to_db()
            updated_game: GameModel = GameModel.find_by_id(game_id)
            self.assertNotEqual(
                game_description_before,
                updated_game.game_description,
                "The user was not updated"
            )
            # delete
            game.delete_from_db()
            self.assertIsNotNone(
                game,
                "User disapered from DB after deletion."
            )
            self.assertTrue(game.hide, "User is not hide after deletion.")
