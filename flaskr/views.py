from flask import jsonify, render_template, request, Blueprint

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("base.html")