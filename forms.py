import pandas as pd

from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField,SelectField
from wtforms.validators import DataRequired

#getting the data
x_data=pd.read_csv('social_network_ads.csv').drop(columns='purchased')

class InputForm(FlaskForm):
    gender=SelectField('Gender',choices=x_data.gender.unique().tolist(),validators=[DataRequired()])
    age=IntegerField('Age',validators=[DataRequired()])
    estimated_salary=IntegerField('Estimated Salary',validators=[DataRequired()])
    submit = SubmitField("Predict")