from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

class SignUpForm(FlaskForm):
    username = StringField(label='username')
    email = StringField(label='email')
    password = PasswordField(label='password')
    confirm_password = PasswordField(label='confirm_password')
    submit = SubmitField(label='submit')