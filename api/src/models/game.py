from src.db import db


class GameModel(db.Model):
    __tablename__ = "games"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        unique=False,
        nullable=True,
        default=1
    )
    game_uid = db.Column(db.Integer, nullable=False)
    game_description = db.Column(db.String(255), nullable=False)
    recommend = db.Column(db.Boolean(), default=0)
    approved = db.Column(db.Boolean(), default=0)
    approved_user_id = db.Column(db.Integer, nullable=False)
    is_random = db.Column(db.Boolean(), default=0)
    is_multiplayer = db.Column(db.Boolean(), default=0)
    number_of_questions = db.Column(db.Integer, nullable=False, default=15)
    hide = db.Column(db.Boolean(), default=False)

    user = db.relationship("UserModel")

    def __init__(self, **kwargs):
        self.user_id = kwargs["user_id"]
        self.game_uid = kwargs["game_uid"]
        self.game_description = kwargs["game_description"]
        self.recommend = kwargs["recommend"] if kwargs.get("recommend") else False  # noqa: E501
        self.approved = kwargs["approved"] if kwargs.get("approved") else False
        self.approved_user_id = kwargs["approved_user_id"] if kwargs.get("approved_user_id") else False  # noqa: E501
        self.is_random = kwargs["is_random"] if kwargs.get("is_random") else False  # noqa: E501
        self.is_multiplayer = kwargs["is_multiplayer"] if kwargs.get("is_multiplayer") else False  # noqa: E501
        self.number_of_questions = kwargs["number_of_questions"] if kwargs.get("number_of_questions") else 15  # noqa: E501
        self.hide = False

    def json(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "game_uid": self.game_uid,
            "game_description": self.game_description,
            "recommend": self.recommend,
            "approved": self.approved,
            "approved_user_id": self.approved_user_id,
            "is_random": self.is_random,
            "is_multiplayer": self.is_multiplayer,
            "number_of_questions": self.number_of_questions,
            "hide": self.hide,
            "user": self.user,
        }

    @classmethod
    def find_all(cls):
        return cls.query.all()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_by_game_uid(cls, game_uid):
        return cls.query.filter_by(game_uid=game_uid).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
