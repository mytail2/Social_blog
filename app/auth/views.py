from . import auth
from .forms import LoginForm, RegisterForm, UnsafeLoginForm
from ..models import User
from flask_login import login_user, logout_user, login_required, current_user
from flask import render_template, redirect, url_for, request, flash
from .. import db
from ..email import send_mail
import sqlite3


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.verify_password(form.password.data):
            login_user(user, form.remember_me)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid username or password.')
    return render_template('auth/login.html', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.index'))

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
 
        token = user.generate_token()
        send_mail(user.email, 'Confirm your account', 'auth/email/confirm', user=user, token=token)
        flash('a confirm email has been sent to your email.')
        return redirect(url_for('main.index'))
    return render_template('auth/register.html', form=form)

@auth.route('/confirm/<token>')
@login_required
def confirm(token):
    if current_user.confirm:
        return redirect(url_for('main.index'))
    if current_user.confirm_token(token):
        flash('You have confirmed your account successfully.')
    else:
        flash('verification failed.')
    return redirect(url_for('main.index'))

@auth.before_app_request
def before_request():
    if current_user.is_authenticated \
        and not current_user.confirm \
            and request.endpoint[:5] != 'auth.':
                return redirect(url_for('auth.unconfirmed'))

@auth.route('/unconfirmed')
def unconfirmed():
    if current_user.is_anonymous or current_user.confirm:
        return redirect(url_for('main.index'))
    return render_template('auth/unconfirmed.html')

@auth.route('/confirm')
@login_required
def resend_confirmation():
    token = current_user.generate_token()
    send_mail(current_user.email, 'Confirm your account', 'auth/email/confirm', user=current_user, token=token)
    flash('a confirm email has been sent to your email.')
    return redirect(url_for('main.index'))


@auth.route('/unsafe/login', methods=['GET', 'POST'])
def unsafe_login():
    form = UnsafeLoginForm()
    if form.validate_on_submit():
        conn = sqlite3.connect('data-dev.sqlite')
        c = conn.cursor() 
        sql = "select * from users where username='%s' and email='%s'" %(form.username.data, form.email.data)
        cursor = c.execute(sql)
        for row in cursor:
            user = User.query.filter_by(username=row[1]).first()
            conn.close()
            login_user(user, form.remember_me)
            return redirect(url_for('main.index'))
        flash('Invalid Infromation.')
    return render_template('auth/login.html', form=form)
    
