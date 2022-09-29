"""Models for Adopt forms"""

from email import message
from email.policy import default
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, FloatField
from wtforms.validators import InputRequired, Optional, NumberRange, URL, AnyOf


class PetForm(FlaskForm):
    """Form for adding a pet"""

    name = StringField('Pet Name', validators=[InputRequired(message="Name cannot be blank")])
    species = StringField('Species', validators=[InputRequired(message="Species cannot be blank"), AnyOf(['dog', 'cat', 'porcupine'], message="Species must be 'dog', 'cat' or 'porcupine'")])
    image_url = StringField('URL of Pet Photo', validators=[Optional(), URL(message="Image URL must be a proper URL")])
    age = IntegerField('Age', validators=[Optional(), NumberRange(min=1, max=30, message="Age must be between 0 and 30")])
    notes = StringField('Additional Notes', validators=[Optional()])
    available = BooleanField('Pet is available', default="checked")

