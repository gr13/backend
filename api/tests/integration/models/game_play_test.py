import sys
# adding src to the system path
from pathlib import Path
sys.path.append(str(Path(sys.path[0]).parent))
sys.path.append(str(Path(sys.path[0]).parent.parent))
sys.path.append(str(Path(sys.path[0]).parent.parent.parent))
# sys.path.append(str(Path(sys.path[0]).parent.parent.parent.parent))
from src.models.game_play import GamePlayModel  # noqa:E402
from tests.base_test import BaseTest  # noqa:E402
from src.models.game import GameModel  # noqa:E402
from src.models.question import QuestionModel  # noqa:E402


class GamePlayTest(BaseTest):
    def _create_question() -> int:
        """
        Creates a standard user to be used in tests
        """
        question = QuestionModel(
            level_id=1,
            difficulty_id=1,
            chapter_id=1,
            sub_chapter_id=1,
            question="test question",
            image_file="",
            answer_a="answer_a",
            answer_b="answer_b",
            answer_c="answer_c",
            answer_d="answer_d",
            correct_answer="A",
            correct_answer_text="correct_answer_text",
            answer_img="answer_img"
        )
        question.save_to_db()
        return question.id

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

    @staticmethod
    def _create_game_play() -> GamePlayModel:
        """
        Creates a game play to be used in tests
        """
        game_id: int = GamePlayTest._create_game()
        question_id: int = GamePlayTest._create_question()
        game_play: GamePlayModel = GamePlayModel(
            user_id=1,
            player_name="player",
            game_id=game_id,
            question_id=question_id,
            answer="A",
            is_answer_correct=True,
        )
        game_play.save_to_db()
        return game_play.id

    def test_crud(self):
        """
        Creates game play and checks that it was added to db correctly
        """
        with self.app_context():
            # create
            game_play_id: int = self._create_game_play()
            # read
            game_play: GamePlayModel = GamePlayModel.find_by_id(game_play_id)
            self.assertIsNotNone(game_play, "Created game_play is not found")
            # update
            game_play_before = game_play.player_name
            game_play.player_name = "player2"
            game_play.save_to_db()
            updated_game_play: GamePlayModel = GamePlayModel.find_by_id(
                game_play_id
            )
            self.assertNotEqual(
                game_play_before,
                updated_game_play.player_name,
                "The user was not updated"
            )
            # delete
            game_play.delete_from_db()
            self.assertIsNotNone(
                game_play,
                "User disapered from DB after deletion."
            )
            self.assertTrue(game_play.hide, "User is not hide after deletion.")

    # def test_game_play_json(self):
    #     """
    #     Creates game play model and checks the returned json
    #     """
    #     game_play = self._create_game_play()
    #     expected = {
    #         "id": None,
    #         "user_id": 1,
    #         "player_name": "player",
    #         "player_id": None,
    #         "game_id": None,
    #         "question_id": 1,
    #         "answer": "A",
    #         "is_answer_correct": False,
    #         "hide": False,
    #         "user": None,
    #         "player": None,
    #         "game": None,
    #         "question": None,
    #     }
    #     actual: Dict = game_play.json()
    #     self.assertDictEqual(actual, expected,
    #         f"User JSON is incorrect expected: {expected}, actual: "
    #             "{actual}")
