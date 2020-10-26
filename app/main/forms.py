from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField,SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, Required
import email_validator

class PitchesForm(FlaskForm):

    text = TextAreaField('Text',validators=[Required()])
    category = SelectField('Type',choices=[('interview','Interview pitch'),('product','Product pitch'),('advertisement','Advertisement')],validators=[Required()])
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Bio.',validators = [Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    text = TextAreaField('Leave a comment:',validators=[Required()])
    submit = SubmitField('Submit')