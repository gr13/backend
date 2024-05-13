import sys
from typing import Dict
# adding src to the system path
from pathlib import Path
sys.path.append(str(Path(sys.path[0]).parent))
sys.path.append(str(Path(sys.path[0]).parent.parent))
sys.path.append(str(Path(sys.path[0]).parent.parent.parent))
# sys.path.append(str(Path(sys.path[0]).parent.parent.parent.parent))
from src.models.game_question import GameQuestionModel  # noqa:E402
from tests.base_test import BaseTest  # noqa:E402


class GameQuestionTest(BaseTest):

    @staticmethod
    def _create_game_question() -> GameQuestionModel:
        """
        Creates a standard user to be used in tests
        """
        return GameQuestionModel(
            game_id=1,
            question_id=1,
            question_order=1,
        )

    def test_create_game_question(self):
        """
        Creates model and checks that email and user name are added correctly
        """
        user = self._create_game_question()
        self.assertEqual(user.game_id, 1,
            "The game_id of the game question after creation does not equal"
            " the constructor argument.")
        self.assertEqual(user.question_id, 1,
            "The question_id of the game question after creation does not "
            "equal the constructor argument.")
        self.assertEqual(user.question_order, 1,
            "The question_order of the game question after creation does not "
            "equal the constructor argument.")

    def test_game_question_json(self):
        """
        Creates user model and checks the returned json
        """
        user = self._create_game_question()
        expected = {
            "id": None,
            "game_id": 1,
            "question_id": 1,
            "question_order": 1,
            "game": None,
            "question": None,
            "hide": False,
        }
        actual: Dict = user.json()
        self.assertDictEqual(actual, expected,
            f"User JSON is incorrect expected: {expected}, actual: "
                "{actual}")
