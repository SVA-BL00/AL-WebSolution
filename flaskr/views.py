from flask import render_template, Blueprint, session, flash, redirect, url_for, request, flash
from werkzeug.security import check_password_hash, generate_password_hash
import functools

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("main.html")

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

@views.route("/search")
def search():
    q = request.args.get("q")
    print(q)

    if q:
        print(q)
        #Nombre del table.query.filter(nombretable.nombre.icontains(q) | nombretable.nombre.icontains(q)).order_by(nombre.idk.asc()).order_by(asdasd)).limit(10).all
    else:
        results = []
    
    return render_template("search_results.html", results=results)