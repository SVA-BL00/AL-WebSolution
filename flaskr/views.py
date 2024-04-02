from flask import render_template, Blueprint, session, flash, redirect, url_for, request
from werkzeug.security import check_password_hash, generate_password_hash
import functools

views = Blueprint('views', __name__)

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
