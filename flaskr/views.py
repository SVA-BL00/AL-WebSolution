from flask import render_template, Blueprint, session, flash, redirect, url_for, request
import os
import string, secrets, smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from werkzeug.security import check_password_hash, generate_password_hash
import functools

views = Blueprint('views', __name__)

## CREACIÓN DE CREDENCIALES PARA USUARIO ##

def send_email(email, password):
    subject = 'Tu información de acceso'
    body = f'\nTu contraseña: {password}'

    message = MIMEMultipart()
    message['From'] = os.getenv('EMAIL_ADDRESS')
    message['To'] = email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP(os.getenv('SMTP_SERVER'), os.getenv('SMTP_PORT')) as server:
        server.starttls()
        server.login(os.getenv('EMAIL_ADDRESS'), os.getenv('APP_PASSWORD'))
        server.sendmail(os.getenv('EMAIL_ADDRESS'), email, message.as_string())

def generate_random_password():
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(8))
    return password

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if 'USER_ID' not in session:
            flash("Por favor ingresa a sesión")
            return redirect(url_for('loginGET'))

        return view(**kwargs)

    return wrapped_view

@views.route('/')
def home():
    return render_template("base.html")

@views.get("/login")
def login_get():
    return render_template("login.html")

@views.post("/login")
def login_post():
    username = request.form['username']
    password = request.form['password']
    # cambiar con función de db / db = get_db()
    error = None
    # user = obten_usuario(db, username)
    #if user is None:
    #    error = 'Usuario incorrecto.'
    # elif not check_password_hash(user['contrasena'], password):
    #   error = 'Contraseña incorrecta.'

    if error is None:
        session.clear()
        ## session['USER_ID'] = user['usuario_id']
        session.permanent = True
        flash('¡Has ingresado correctamente!')
        return redirect(url_for('/'))
    #flash(error)
    return redirect(url_for('login_get'))
