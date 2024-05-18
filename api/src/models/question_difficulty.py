from src.db import db


class QuestionDifficultyModel(db.Model):
    __tablename__ = "question_difficulties"

    id = db.Column(db.Integer, primary_key=True)
    difficulty = db.Column(db.Integer, nullable=False, unique=True)
    difficulty_name = db.Column(db.String(10), nullable=False, unique=True)
    hide = db.Column(db.Boolean(), default=False)

    def __init__(self, difficulty: int, difficulty_name: str):
        self.difficulty = difficulty
        self.difficulty_name = difficulty_name
        self.hide = False

    def json(self):
        return {
            "id": self.id,
            "difficulty": self.difficulty,
            "difficulty_name": self.difficulty_name,
            "hide": self.hide,
        }

    @classmethod
    def find_all(cls):
        return cls.query.all()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_by_difficulty(cls, difficulty: int):
        return cls.query.filter_by(difficulty=difficulty).first()

    # def save_to_db(self):
    #     db.session.add(self)
    #     db.session.commit()
