from flask import render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from app.models import Product
from app import app, db



@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        product = Product(text=request.form['input'])
        db.session.add(product)
        db.session.commit()
        return redirect(url_for('home'))
    products = Product.query.all()
    return render_template('home.html', products=products)
