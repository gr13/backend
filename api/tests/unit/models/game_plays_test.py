import sys
from typing import Dict
# adding src to the system path
from pathlib import Path
sys.path.append(str(Path(sys.path[0]).parent))
sys.path.append(str(Path(sys.path[0]).parent.parent))
sys.path.append(str(Path(sys.path[0]).parent.parent.parent))
# sys.path.append(str(Path(sys.path[0]).parent.parent.parent.parent))
from src.models.game_play import GamePlayModel  # noqa:E402
from tests.base_test import BaseTest  # noqa:E402


class GamePlayTest(BaseTest):

    @staticmethod
    def _create_game_play() -> GamePlayModel:
        """
        Creates a game play to be used in tests
        """
        return GamePlayModel(
            user_id=1,
            player_name="player",
            question_id=1,
            answer="A",
            is_answer_correct=False,
        )

    def test_create_game_play(self):
        """
        Creates model and checks that fields are added correctly
        """
        game_play = self._create_game_play()
        self.assertEqual(game_play.player_name, "player",
            "The player_name of the game play after creation does not equal"
            " the constructor argument.")
        self.assertEqual(game_play.question_id, 1,
            "The question_id of the game play after creation does not "
            "equal the constructor argument.")

    def test_game_play_json(self):
        """
        Creates game play model and checks the returned json
        """
        game_play = self._create_game_play()
        expected = {
            "id": None,
            "player_name": "player",
            "player_id": None,
            "game_id": None,
            "question_id": 1,
            "answer": "A",
            "is_answer_correct": False,
            "hide": False,
        }
        actual: Dict = game_play.json()
        self.assertDictEqual(actual, expected,
            f"User JSON is incorrect expected: {expected}, actual: "
                "{actual}")
