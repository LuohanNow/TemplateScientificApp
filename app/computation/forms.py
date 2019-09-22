from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField
from wtforms import validators
from math import pi

class InputForm(FlaskForm):

    A = FloatField(label='amplitude (m)', default=1.0, validators=[validators.NumberRange(-5, 5, message='-5;5')])

    b = FloatField(label='damping factor (kg/s)', default=0, validators=[validators.InputRequired()])

    w = FloatField(label='frequency (1/s)', default=2*pi, validators=[validators.InputRequired()])

    T = FloatField(label='time interval (s)', default=18, validators=[validators.InputRequired()])

    compute = SubmitField('Compute')