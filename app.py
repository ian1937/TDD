from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    app.config['DEBUG'] = True

    with app.app_context():
        db.init_app(app)
        return app

app = create_app()


@app.route('/')
def home():
    return render_template('home.html', data="Say Hello")


if __name__ == "__main__":
    app.run()
