from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField
from wtforms.validators import DataRequired, Length, Email

class ContactForm(FlaskForm):
    name = StringField('Name', [DataRequired()])
    email = TextField("Email",  [DataRequired("Please enter your email address."),
                                 Email("Please enter your email address.")])
    body = TextField('Message', [
        DataRequired(),
        Length(min=4, message=('Your message is too short.'))])
    submit = SubmitField('Submit')

