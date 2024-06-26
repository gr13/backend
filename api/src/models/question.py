from src.db import db


class QuestionModel(db.Model):
    __tablename__ = "questions"

    id = db.Column(db.Integer, primary_key=True)
    level_id = db.Column(
        db.Integer,
        db.ForeignKey("question_levels.id"),
        unique=False,
        nullable=False,
    )
    difficulty_id = db.Column(
        db.Integer,
        db.ForeignKey("question_difficulties.id"),
        unique=False,
        nullable=False,
    )
    chapter_id = db.Column(
        db.Integer,
        db.ForeignKey("chapters.id"),
        unique=False,
        nullable=False,
    )
    sub_chapter_id = db.Column(
        db.Integer,
        db.ForeignKey("sub_chapters.id"),
        unique=False,
        nullable=False,
    )
    question = db.Column(db.String(255), nullable=False)
    image_file = db.Column(db.String(20), nullable=False)
    answer_1 = db.Column(db.String(255), nullable=False)
    answer_2 = db.Column(db.String(255), nullable=False)
    answer_3 = db.Column(db.String(255), nullable=False)
    answer_4 = db.Column(db.String(255), nullable=False)
    answer_time = db.Column(db.Integer, nullable=False, default=60)
    correct_answer = db.Column(db.Integer, nullable=False)
    correct_answer_text = db.Column(db.String(255), nullable=False)
    answer_img = db.Column(db.String(20), nullable=False)
    is_error = db.Column(db.Boolean(), default=False)
    is_validated = db.Column(db.Boolean(), default=False)
    hide = db.Column(db.Boolean(), default=False)

    level = db.relationship("QuestionLevelModel")
    difficulty = db.relationship("QuestionDifficultyModel")
    chapter = db.relationship("ChapterModel")
    sub_chapter = db.relationship("SubChapterModel")

    def __init__(self, **kwargs):
        """
        init
        """
        self.level_id = kwargs["level_id"]
        self.difficulty_id = kwargs["difficulty_id"]
        self.chapter_id = kwargs["chapter_id"]
        self.sub_chapter_id = kwargs["sub_chapter_id"]
        self.question = kwargs["question"]
        self.image_file = kwargs["image_file"]
        self.answer_1 = kwargs["answer_1"]
        self.answer_2 = kwargs["answer_2"]
        self.answer_3 = kwargs["answer_3"]
        self.answer_4 = kwargs["answer_4"]
        self.answer_time = kwargs["answer_time"] if kwargs.get("answer_time") else 30  # noqa: E501
        self.correct_answer = kwargs["correct_answer"]
        self.correct_answer_text = kwargs["correct_answer_text"]
        self.answer_img = kwargs["answer_img"]
        self.is_validated = 0
        self.is_error = 0
        self.hide = 0

    def json(self):
        return {
            "id": self.id,
            "level_id": self.level_id,
            "difficulty_id": self.difficulty_id,
            "chapter_id": self.chapter_id,
            "sub_chapter_id": self.sub_chapter_id,
            "question": self.question,
            "image_file": self.image_file,
            "answer_1": self.answer_1,
            "answer_2": self.answer_2,
            "answer_3": self.answer_3,
            "answer_4": self.answer_4,
            "answer_time": self.answer_time,
            "correct_answer": self.correct_answer,
            "correct_answer_text": self.correct_answer_text,
            "answer_img": self.answer_img,
            "is_validated": self.is_validated,
            "level": self.level,
            "difficulty": self.difficulty,
            "chapter": self.chapter,
            "sub_chapter": self.sub_chapter,
            "is_error": self.is_error,
            "hide": self.hide,
        }

    @classmethod
    def find_all(cls):
        return cls.query.all()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        self.hide = True
        self.save_to_db()
