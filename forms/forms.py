from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField

class PassGenerator(FlaskForm):
    passLength = IntegerField('Password Lenght')
    submit = SubmitField('Generate password')
