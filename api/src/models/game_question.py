from src.db import db


class GameQuestionModel(db.Model):
    __tablename__ = "game_questions"

    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(
        db.Integer,
        db.ForeignKey("games.id"),
        unique=False,
        nullable=False,
    )
    question_id = db.Column(
        db.Integer,
        db.ForeignKey("questions.id"),
        unique=False,
        nullable=False,
    )
    question_order = db.Column(db.Integer, nullable=False)

    hide = db.Column(db.Boolean(), default=False)

    game = db.relationship("GameModel")
    question = db.relationship("QuestionModel")

    def __init__(self, **kwargs):
        self.game_id = kwargs["game_id"]
        self.question_id = kwargs["question_id"]
        self.question_order = kwargs["question_order"]
        self.hide = False

    def json(self):
        return {
            "id": self.id,
            "game_id": self.game_id,
            "question_id": self.question_id,
            "question_order": self.question_order,
            "game": self.game,
            "question": self.question,
            "hide": self.hide,
        }

    @classmethod
    def find_all(cls):
        return cls.query.all()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_by_game(cls, game_id):
        return cls.query.filter_by(game_id=game_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()