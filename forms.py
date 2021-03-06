from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired(), Length(min= 5, max= 20)])
    fname = StringField('First Name', validators = [DataRequired(), Length(min= 3, max= 40)])
    lname = StringField('Last Name', validators = [DataRequired(), Length(min= 3, max= 40)])
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    confirmPassword = PasswordField('Confirm Password', validators = [DataRequired(), EqualTo('password')])

    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class SearchForm(FlaskForm):
    book = StringField("ISBN, Title or Author", validators = [DataRequired()])
    submit = SubmitField('Search')


class BookDetailForm(FlaskForm):
    comment = StringField("Comment about the Book", validators = [DataRequired()])
    rating = SelectField("Rating", choices = [('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5)], default= '3')
    submit = SubmitField("Submit")