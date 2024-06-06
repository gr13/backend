# import logging
from src.db import db
from src.models.user_right import UserRightModel # noqa
from sqlalchemy.orm import validates
from werkzeug.security import generate_password_hash, check_password_hash

import secrets


class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(256))
    right_id = db.Column(
        db.Integer,
        db.ForeignKey("rights.id"),
        unique=False,
        nullable=False,
        default=1
    )
    right = db.relationship(
        "UserRightModel",
        back_populates="users",
    )

    username = db.Column(db.String(10), default="")
    position = db.Column(db.String(100), default="")

    can_validate = db.Column(db.Boolean(), default=False, nullable=False)
    can_edit = db.Column(db.Boolean(), default=False, nullable=False)
    can_seelog = db.Column(db.Boolean(), default=False, nullable=False)
    can_seeusers = db.Column(db.Boolean(), default=False, nullable=False)

    hide = db.Column(db.Boolean(), default=False, nullable=False)
    log_user_id = db.Column(db.Integer, nullable=False)
    log_comment = db.Column(db.String(255), default="")

    @validates("email")
    def validate_email(self, key, email):
        assert "@" in email
        return email

    def __init__(self, **kwargs):
        self.email = kwargs["email"]
        self.username = kwargs["username"]
        self.password = self.set_password(kwargs["password"])
        self.right_id = 2
        self.position = "Not in use"
        self.can_validate = 0
        self.can_edit = 0
        self.can_seelog = 0
        self.can_seeusers = 0
        self.hide = 0
        self.log_user_id = 0
        self.log_comment = "testing"

    def json(self):
        """
        Return json representation of the class
        """
        return {
            "id": self.id,
            "email": self.email,
            "right_id": self.right_id,
            "right": self.right.json() if self.right else None,
            "username": self.username,
            "can_validate": self.can_validate,
            "can_edit": self.can_edit,
            "can_seelog": self.can_seelog,
            "can_seeusers": self.can_seeusers,
            "hide": self.hide,
            "log_user_id": self.log_user_id,
            "log_comment": self.log_comment,
        }

    @classmethod
    def find_by_email(cls, email: str):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def find_by_id(cls, _id: int):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        self.hide = True
        self.save_to_db()

    def set_password(self, _password: str):
        """
        sets password
        """
        self.password = generate_password_hash(_password)

    def check_password(self, _password: str) -> bool:
        """
        checks if password is right
        """
        return check_password_hash(self.password, _password)

    @classmethod
    def create_random_password(cls):
        return secrets.token_hex(8)
