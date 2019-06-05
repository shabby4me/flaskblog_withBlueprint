import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from flaskblog import mail

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn)
    #scale down the size
    output_size = (125,125)
    tn = Image.open(form_picture)
    tn.thumbnail(output_size)
    
    tn.save(picture_path)
    return picture_fn

def send_reset_email(user):
    token =  user.get_reset_token()
    msg = Message('Password Reset Request',
                  sender='lyz625747835@gmail.com',
                  recipients=[user.email])
    msg.body = '''To reset your password, visit the following link in 10 min:
{}

If you did not make the request then just ignore this email.
'''.format(url_for('users.reset_password', token=token, _external=True))
    mail.send(msg)
