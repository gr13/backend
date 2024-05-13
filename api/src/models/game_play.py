from src.db import db


class GamePlayModel(db.Model):
    __tablename__ = "game_plays"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=True, unique=False)
    player_name = db.Column(db.String(5), nullable=False)
    player_id = db.Column(db.Integer, nullable=True, unique=False)
    game_id = db.Column(db.Integer, nullable=True, unique=False)
    question_id = db.Column(db.Integer, nullable=True, unique=False)
    answer = db.Column(db.String(1))
    is_answer_correct = db.Column(db.Boolean(), default=0)

    # lazy="dynamic" does not create the list of items
    # unless it is necessary
    # users = db.relationship(
    #     "UserModel", lazy="dynamic", back_populates="rights"
    # )

    def __init__(self, user_right):
        self.user_right = user_right

    def json(self):
        return {
            "id": self.id,
            "player_name": self.player_name,
            "player_id": self.player_id,
            "game_id": self.game_id,
            "question_id": self.question_id,
            "answer": self.answer,
            "is_answer_correct": self.is_answer_correct,
        }

    @classmethod
    def find_all(cls):
        return cls.query.all()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_by_game_id(cls, game_id):
        return cls.query.filter_by(game_id=game_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()