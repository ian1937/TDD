from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class ProductForm(FlaskForm):
    name = StringField("Product Name")
    submit = SubmitField("Add")