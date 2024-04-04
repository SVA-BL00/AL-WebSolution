from flask import Flask
import pyodbc
from dotenv import load_dotenv
import os
import secrets 


def create_app():
    app = Flask(__name__)
    app._static_folder = 'static'
    load_dotenv()

    app.config['SECRET_KEY'] = secrets.token_hex(16)

    from .views import views
    app.register_blueprint(views, url_prefix='/')

    return app
