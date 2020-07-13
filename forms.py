from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo


class SubmitForm(FlaskForm):
    username = StringField('Name',validators=[DataRequired(), Length(min=2, max=20)])

    email = StringField('Email',validators=[DataRequired()])

    horsepower = StringField('Horsepower (>50bhp):',validators=[DataRequired(), Length(min=1, max=20)])

    cylinders = StringField('No. of cylinders (3-8):', validators=[DataRequired(), Length(min=1, max=20)])

    mileage = StringField('Mileage (15-25 kmpl):', validators=[DataRequired(), Length(min=1, max=20)])

    manual = BooleanField('Manual transmission:(default Auto)')

    gears = StringField('No. of Gears (3-6):', validators=[DataRequired(), Length(min=1, max=20)]) 

    seats = StringField('Curb Weight (1-4 tons):', validators=[DataRequired(), Length(min=1, max=20)]) 
    
    submit = SubmitField('Search')
