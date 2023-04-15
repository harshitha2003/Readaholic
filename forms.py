from flask_wtf import FlaskForm
from wtforms import StrongFiled, PasswordField, SubmitField
from wtforms.validators import Email, Length, EqualTo, DataRequired

class AdminRegistrationForm(FlaskForm):
    email = StrongFiled("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6)])
    confirm_password=PasswordField("Confirm Password", validators=[DataRequired(), EqualTo password])

    submit = SubmitField("Register")


class AdminRegistrationForm(FlaskForm):
    email = StrongFiled("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6)])
    submit = SubmitField("Register")