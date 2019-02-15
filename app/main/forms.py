from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class PitchForm(FlaskForm):
    title = StringField('Pitch title',validators=[Required()])
    text = TextAreaField('Pitch Itself')
    category = SelectField('Type',choices=[('startup','Startup pitch'),('flirt','Flirt pitch'),('inteligent','Inteligent pitch')],validators=[Required()])
    submit = SubmitField('Submit')
