from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User

class LoginForm(FlaskForm):
    email = StringField('email', validators=[Length(1, 64), Email()])
    password = PasswordField('password', validators=[DataRequired()])
    remember_me = BooleanField('keep me login in')
    submit = SubmitField('log_in')


class RegisterForm(FlaskForm):

    email = StringField('Email', validators=[ DataRequired(), Length(1, 64), Email() ])
    username = StringField('Username', validators=[ DataRequired(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, 'Usernames must have only letters, numbers, dots or underscores.') ])
    password = PasswordField('Password', validators=[ DataRequired(), EqualTo('password2', 'Passwords must match.') ])
    password2 = PasswordField('Confirm Password', validators=[ DataRequired() ])
    submit = SubmitField('Register')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first() is not None:
            raise ValidationError('Email already registered.')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already registered.')

class UnsafeLoginForm(FlaskForm):
    username = StringField('username')
    email = PasswordField('email')
    remember_me = BooleanField('keep me login in')
    submit = SubmitField('log_in')


            
    
    
