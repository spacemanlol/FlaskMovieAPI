from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Two API Endpoints:
# 1) View All Movies
# 2) Add a movie

db = SQLAlchemy()
# Init
def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

    db.init_app(app)

    # Imported here to avoid circular inputs, flask app needs to be created first
    from .views import main
    app.register_blueprint(main)

    return app


