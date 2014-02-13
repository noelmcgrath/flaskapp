from flask.ext.wtf import Form
from wtforms import StringField
from wtforms import SubmitField
from wtforms import Form, BooleanField, StringField, validators

class ContactForm(Form):
  name = StringField("Name", [validators.Length(min=6, message=('Little short for a name?'))])
  email = StringField("Email", [validators.Length(min=6, message=('Little short for an email address?')),
    validators.Email(message=('That\'s not a valid email address.'))])
  subject = StringField("Subject", [validators.Length(min=6, message=('Little short for a subject?'))])
  submit = SubmitField("Send")
