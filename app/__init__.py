from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import config


db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    

    with app.app_context():
        from app.models import Product

        db.init_app(app)
        db.drop_all()
        db.create_all()

        from app import product


    return app
