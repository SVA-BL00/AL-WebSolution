from flask import render_template, Blueprint, session, flash, redirect, url_for, request
import functools
from .db import get_db_connection

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("main.html")

@views.get('/login')
def loginGET():
    return render_template("login.html")

@views.post('/login')
def loginPOST():
    usermail = request.form.get('userMail')
    password = request.form.get('password')

    conn = get_db_connection()
    if not conn:
        flash("Failed to connect to database", 'error')
        return redirect(url_for('loginGET'))

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Employees WHERE Email = ?", (usermail,))
        user = cursor.fetchone()

        if user and user[5] == password:  
            session.clear()
            session['USER_ID'] = user[0]  
            session.permanent = True
            flash('¡Has ingresado correctamente!', 'success')
            return redirect(url_for('views.home'))
        else:
            flash('Usuario o contraseña incorrectos', 'error')
    except Exception as e:
        flash('Error al intentar iniciar sesión', 'error')
        print(f"Error: {e}")
    finally:
        conn.close()
    return render_template("login.html")    

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