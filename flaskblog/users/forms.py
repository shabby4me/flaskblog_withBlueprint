from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from flaskblog.models import User


class RegistrationForm(FlaskForm):
    username = StringField('username *',
                           validators=[DataRequired(), Length(min=5, max=20)])
    email = StringField('Email *',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password *', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password *',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

##    def validate_field(self,field):
##        if True:
##            raise ValidationError('Validation Message')
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username taken, please choose another username')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email taken, please choose another username')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
    
class UpdateAccountForm(FlaskForm):
    username = StringField('username *',
                           validators=[DataRequired(), Length(min=5, max=20)])
    email = StringField('Email *',
                        validators=[DataRequired(), Email()])
    picture = FileField('Update profile picture', validators=[FileAllowed(['jpg','png','bmp'])])
    update = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('Username taken, please choose another username')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Email taken, please choose another username')



class RequestResetForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('Account with the email does not exist, please check your email')

class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password *', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password *',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')
