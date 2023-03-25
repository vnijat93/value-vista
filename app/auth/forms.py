from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from ..models import User
from wtforms import ValidationError


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Length(8, 64), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Keep me logged in")
    submit = SubmitField("Log in")


class RegistrationForm(FlaskForm):
    full_name = StringField(
        "Full Name",
        validators=[
            DataRequired(),
            Length(8, 64),
            Regexp(
                "^[A-Z][a-z]+\s[A-Z][a-z]+$",
                0,
            ),
        ],
    )

    email = StringField("Email", validators=[DataRequired(), Length(8, 64), Email()])

    username = StringField(
        "Username",
        validators=[
            DataRequired(),
            Length(5, 64),
            Regexp(
                "^[A-Za-z][A-Za-z0-9_]*$",
                0,
                "Username must have only letters, numbers, or underscores",
            ),
        ],
    )
    password = PasswordField(
        "Password",
        validators=[
            DataRequired(),
            EqualTo("password2", message="Password must match"),
        ],
    )
    password2 = PasswordField("Conform Password", validators=[DataRequired()])
    submit = SubmitField("Register")

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError("Email already registered.")

    def validate_name(self, filed):
        if User.query.filter_by(name=filed.data).first():
            raise ValidationError("Username already in use")
