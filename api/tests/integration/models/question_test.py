import sys
# adding src to the system path
from pathlib import Path
sys.path.append(str(Path(sys.path[0]).parent))
sys.path.append(str(Path(sys.path[0]).parent.parent))
sys.path.append(str(Path(sys.path[0]).parent.parent.parent))
# sys.path.append(str(Path(sys.path[0]).parent.parent.parent.parent))
from src.models.question import QuestionModel  # noqa:E402
from tests.base_test import BaseTest  # noqa:E402


class UserTest(BaseTest):
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

    def test_crud(self):
        """
        Creates model and checks that it was added to db correctly
        """
        with self.app_context():
            # create
            question_id: int = self._create_question()
            # read
            question: QuestionModel = QuestionModel.find_by_id(question_id)
            self.assertIsNotNone(question, "Created user is not found")
            # update
            question_name_before = question.question
            question.question = "question2"
            question.save_to_db()
            updated_question: QuestionModel = QuestionModel.find_by_id(
                question_id)
            self.assertNotEqual(
                question_name_before,
                updated_question.question,
                "The question was not updated"
            )
            # delete
            question.delete_from_db()
            self.assertIsNotNone(
                question,
                "Question disapered from DB after deletion."
            )
            self.assertTrue(
                question.hide, "Question is not hide after deletion.")
