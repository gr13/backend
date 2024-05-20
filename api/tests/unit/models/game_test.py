import sys
from typing import Dict
# adding src to the system path
from pathlib import Path
sys.path.append(str(Path(sys.path[0]).parent))
sys.path.append(str(Path(sys.path[0]).parent.parent))
sys.path.append(str(Path(sys.path[0]).parent.parent.parent))
# sys.path.append(str(Path(sys.path[0]).parent.parent.parent.parent))
from src.models.game import GameModel  # noqa:E402
from tests.base_test import BaseTest  # noqa:E402


class GameTest(BaseTest):

    @staticmethod
    def _create_game() -> GameModel:
        """
        Creates a standard user to be used in tests
        """
        return GameModel(
            user_id=1,
            game_description="description",
        )

    def test_create_game(self):
        """
        Creates model and checks that email and user name are added correctly
        """
        game = self._create_game()
        self.assertEqual(game.user_id, 1,
            "The user_id of the game after creation does not equal"
            " the constructor argument.")
        self.assertEqual(game.game_description, "description",
            "The game_description of the game after creation does not "
            "equal the constructor argument.")

    def test_game_json(self):
        """
        Creates game model and checks the returned json
        """
        game = self._create_game()
        expected = {
            "id": None,
            "user_id": 1,
            "game_uid": "uuid",
            "game_description": "description",
            "recommend": False,
            "approved": False,
            "approved_user_id": False,
            "is_random": False,
            "is_multiplayer": False,
            "number_of_questions": 15,
            "hide": False,
            "user": None,
        }
        actual: Dict = game.json()
        expected["game_uid"] = actual["game_uid"]
        self.assertDictEqual(actual, expected,
            f"User JSON is incorrect expected: {expected}, actual: "
                "{actual}")
