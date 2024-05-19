from src.db import db


class GamePlayModel(db.Model):
    __tablename__ = "game_plays"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        unique=False,
        nullable=True,
    )
    player_name = db.Column(db.String(10), nullable=False)
    player_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        unique=False,
        nullable=True,
    )
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
        nullable=True,
    )
    answer = db.Column(db.String(1))
    is_answer_correct = db.Column(db.Boolean(), default=0)
    hide = db.Column(db.Boolean(), default=False)

    user = db.relationship(
        "UserModel", primaryjoin="UserModel.id == GamePlayModel.user_id"
    )
    player = db.relationship(
        "UserModel", primaryjoin="UserModel.id == GamePlayModel.player_id"
    )
    game = db.relationship(
        "GameModel", primaryjoin="GameModel.id == GamePlayModel.game_id"
    )
    question = db.relationship(
        "QuestionModel",
        primaryjoin="QuestionModel.id == GamePlayModel.question_id"
    )

    def __init__(self, **kwargs):
        self.user_id = kwargs["user_id"]
        self.player_name = kwargs["player_name"]
        self.player_id = kwargs["player_id"] if kwargs.get("player_id") else None  # noqa: E501
        self.game_id = kwargs["game_id"]
        self.question_id = kwargs["question_id"]
        self.answer = kwargs["answer"]
        self.is_answer_correct = kwargs["is_answer_correct"]
        self.hide = False

    def json(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "player_name": self.player_name,
            "player_id": self.player_id,
            "game_id": self.game_id,
            "question_id": self.question_id,
            "answer": self.answer,
            "is_answer_correct": self.is_answer_correct,
            "hide": self.hide,
            "user": self.user,
            "player": self.player,
            "game": self.game,
            "question": self.question,
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

    def delete_from_db(self):
        self.hide = True
        self.save_to_db()
