from flask import render_template, current_app
from . import mail
from flask_mail import Message
def send_mail(to, subject, template, **kwargs):
    msg = Message(current_app.config['FLASKY_MAIL_SUBJECT_PREFIX']+subject, sender=current_app.config['FLASKY_MAIL_SENDER'], recipients=[to])
    msg.body = render_template(template+'.txt', **kwargs)
    msg.html = render_template(template+'.html', **kwargs)
    mail.send(msg)
    
    
    
