from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, \
        SelectField, BooleanField
from wtforms.validators import DataRequired, Length, Email, Regexp, \
        ValidationError
from flask_wtf.file import FileField, FileAllowed, FileRequired
from ..models import User, Role
from flask_pagedown.fields import PageDownField


class EditProfileForm(FlaskForm):
    name = StringField('Real name', validators=[Length(0, 64)])
    location = StringField('Location', validators=[Length(0, 64)])
    about_me = TextAreaField('About me')
    submit = SubmitField('Submit')


class EditProfileAdminForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64), Email()])
    username = StringField('Username', validators=[DataRequired(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, 'Username must only have letters, numbers, underscores and dots.')])
    confirm = BooleanField('Confirm')
    role = SelectField('Role', coerce=int)
    name = StringField('Real name', validators=[Length(0, 64)])
    location = StringField('Location', validators=[Length(0, 64)])
    about_me = TextAreaField('About me')
    submit = SubmitField('Submit')

    def __init__(self, user, *args, **kwargs):
        super(EditProfileAdminForm, self).__init__(*args, **kwargs)
        self.role.choices = [(role.id, role.name) for role in Role.query.order_by(Role.name).all()]
        self.user = user

    def validate_email(self, field):
        if field.data != self.user.email and \
                User.query.filter_by(email=field.data).first():
                    raise ValidationError('Email already registered.')

    def validate_username(self, field):
        if field.data != self.user.username and \
                User.query.filter_by(username=field.data).first():
                    raise ValidationError('Username already in use.')


class PostForm(FlaskForm):
    body = PageDownField("What's on your mind", validators=[DataRequired()])
    submit = SubmitField('Submit')


class CommentForm(FlaskForm):
    body = StringField('Enter your comment', validators=[DataRequired()])
    submit = SubmitField('Submit')


class UploadForm(FlaskForm):
        file = FileField('Upload file', validators=[FileAllowed(['txt', 'png', 'jpg', 'xls', 'JPG', 'PNG', 'xlsx', 'gif', 'GIF'], 'File format incorrect'), FileRequired()])
        submit = SubmitField('Submit')

class UnsafeUploadForm(FlaskForm):
        file = FileField('Upload file', validators=[FileRequired()])
        submit = SubmitField('Submit')

class UnsafeEditProfileForm(FlaskForm):
    name = StringField('Real name')
    location = StringField('Location')
    about_me = TextAreaField('About me')
    submit = SubmitField('Submit')


class UnsafeCommandForm(FlaskForm):
    command = StringField('Enter Ip')
    submit = SubmitField('Submit')


class CommandForm(FlaskForm):
    command = StringField('Enter Ip', validators=[Regexp('^[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3} -c 4$', 0, 'Invalid Ip address')])
    submit = SubmitField('Submit')



