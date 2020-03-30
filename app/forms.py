from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email


class DepartmentForm(FlaskForm):
    dept_name = StringField('Name', validators=[DataRequired()])
    building = StringField('Building', validators=[DataRequired()])
    budget = StringField('Budget')
    submit = SubmitField('Save')


class StudentForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    dept_name = SelectField('Department', choices=[('', '')])
    submit = SubmitField('Save')
