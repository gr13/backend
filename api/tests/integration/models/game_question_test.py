import sys

# adding src to the system path
from pathlib import Path
sys.path.append(str(Path(sys.path[0]).parent))
sys.path.append(str(Path(sys.path[0]).parent.parent))
sys.path.append(str(Path(sys.path[0]).parent.parent.parent))
# sys.path.append(str(Path(sys.path[0]).parent.parent.parent.parent))
from src.models.game_question import GameQuestionModel  # noqa:E402
from tests.base_test import BaseTest  # noqa:E402
from src.models.question import QuestionModel  # noqa:E402
from src.models.game import GameModel  # noqa:E402


class GameQuestionTest(BaseTest):
    @staticmethod
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
            answer_1="answer_1",
            answer_2="answer_2",
            answer_3="answer_3",
            answer_4="answer_4",
            correct_answer=1,
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
    def _create_game_question() -> int:
        """
        Creates a standard user to be used in tests
        """

        game_question = GameQuestionModel(
            game_id=GameQuestionTest._create_game(),
            question_id=GameQuestionTest._create_question(),
            question_order=1,
        )
        game_question.save_to_db()
        return game_question.id

    def test_crud(self):
        """
        Creates model and checks that it was added to db correctly
        """
        with self.app_context():
            # create
            game_question_id: int = self._create_game_question()
            # read
            game_question: GameQuestionModel = GameQuestionModel.find_by_id(
                game_question_id
            )
            self.assertIsNotNone(game_question, "Created user is not found")
            # update
            game_question_before = game_question.question_order
            game_question.question_order = 2
            game_question.save_to_db()
            updated_game_question = GameQuestionModel.find_by_id(
                game_question_id
            )
            self.assertNotEqual(
                game_question_before,
                updated_game_question.question_order,
                "The game_question was not updated"
            )
            # delete
            game_question.delete_from_db()
            self.assertIsNotNone(
                game_question,
                "game_question disapered from DB after deletion."
            )
            self.assertTrue(
                game_question.hide, "game_question is not hide after deletion."
            )
