from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, FileField, SelectField, widgets, TextAreaField
from flask_wtf.file import FileAllowed, FileRequired
from wtforms.validators import DataRequired, URL, Length, Email, ValidationError


class ContactForm(FlaskForm):
    name = StringField("name", validators=[DataRequired()])
    email = StringField("email", validators=[DataRequired(), Email()])
    message = TextAreaField("message", validators=[DataRequired()])
    send_message = SubmitField()