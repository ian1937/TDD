from flask import render_template, request, redirect, url_for, current_app
from flask_sqlalchemy import SQLAlchemy
from app.models import Product
from app import db
from app.forms import ProductForm



@current_app.route('/', methods=['GET', 'POST'])
def home():
    form = ProductForm
    products = Product.query.all()
    if request.method == 'POST':
        product = Product(name=request.form['input'])
        db.session.add(product)
        db.session.commit()
        products = Product.query.all()
        return render_template('home.html', products=products, form=form)
    return render_template('home.html', products=products, form=form)
