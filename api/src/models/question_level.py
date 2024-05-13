from src.db import db


class QuestionLevelModel(db.Model):
    __tablename__ = "question_levels"

    id = db.Column(db.Integer, primary_key=True)
    question_level = db.Column(
        db.Integer,
        nullable=False,
        default=0,
        unique=True
    )

    def __init__(self, question_level):
        self.question_level = question_level

    def json(self):
        return {
            "id": self.id,
            "level": self.question_level
        }

    @classmethod
    def find_all(cls):
        return cls.query.all()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_by_level(cls, level):
        return cls.query.filter_by(question_level=level).first()
