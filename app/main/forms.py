from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

# class PitchForm(FlaskForm):
#     message = TextAreaField('Pitch',validators=[Required()])
#     submit = SubmitField('Submit')
