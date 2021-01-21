from flask import render_template, request, redirect, url_for, current_app
from flask_sqlalchemy import SQLAlchemy
from app.models import Product
from app import db
from app.forms import ProductForm



@current_app.route('/', methods=['GET', 'POST'])
def product():
    form = ProductForm()
    if request.method == 'POST':
        product = Product(name=form.name.data)
        db.session.add(product)
        db.session.commit()
    products = Product.query.all()
    return render_template('home.html', products=products, form=form)


@current_app.route('/delete/<int:id>', methods=['POST'])
def delete_product(id):
    product = Product.query.filter_by(id=id).first_or_404()
    db.session.delete(product)
    db.session.commit()
    return redirect(url_for('product'))