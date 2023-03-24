from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class Poke_Name(FlaskForm):
    poke_name = StringField('Pokemon_Name')
    submit = SubmitField()