from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo

class UserForm(FlaskForm):
    user = StringField('Search for an Opponet!', validators=[DataRequired()], render_kw={'placeholder': 'Search for an Opponet!'})
    submit = SubmitField('Search')

class Poke_Name(FlaskForm):
    poke_name = StringField('Search for Pokemon')
    submit = SubmitField()

class SignUpForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired()])
    email = StringField('Email', validators = [DataRequired()])
    password = PasswordField('Password', validators = [DataRequired()])
    confirm_password = PasswordField("Confirm", validators = [DataRequired(), EqualTo('password')])
    submit = SubmitField()

class LoginForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired()])
    password = PasswordField('Password', validators = [DataRequired()])
    submit = SubmitField()

