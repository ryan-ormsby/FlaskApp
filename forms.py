from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class AddRiskForm(FlaskForm):
    orderid = StringField('orderid', validators=[DataRequired()])

class AddReviewForm(FlaskForm):
    nickname = StringField('nickname', validators=[DataRequired()])
    review = StringField('review', validators=[DataRequired()])
