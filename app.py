from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from models import Item


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


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        item = Item(text=request.form['input'])
        db.session.add(item)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('home.html', data="Say Hello")


if __name__ == "__main__":
    app.run()
