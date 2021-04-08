from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField, IntegerField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    login_email = EmailField('Login / email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password_again = PasswordField('Repeat password', validators=[DataRequired()])
    surname = StringField('Surname', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired()])
    position = TextAreaField("Position")
    speciality = TextAreaField("Speciality")
    address = TextAreaField("Address")
    submit = SubmitField('Войти')