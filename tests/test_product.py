import os
import pytest
import tempfile
from app import create_app, db
from flask import current_app
from app.models import Product


class TestBase:
    @pytest.fixture(scope='session', autouse=True)
    def client(self):
        app = create_app('test')

        with app.app_context():
            with current_app.test_client() as client:
                db.drop_all()
                db.create_all()
                yield client


    def response_data(self, client):
        response = client.get('/')
        content = response.data
        return content


class TestView(TestBase):
    @pytest.mark.parametrize("attribute", [
        b"html",
        b"head",
        b"css",
        b"body",
        b"form",
        b"input",
        b"submit"
    ])

    def test_has_attribute(self, client, attribute):
        assert (attribute) in self.response_data(client)

    def test_takes_POST_request(self, client):
        response = client.post('/', data={'name': 'Say Hello'})
        assert b"Say Hello" in self.response_data(client)


class TestDatabase(TestBase):
    def test_database_is_working(self):
        product1 = Product(name="First Product")
        product2 = Product(name="Second Product")

        db.session.add(product1)
        db.session.add(product2)

        db.session.commit()

        product_1 = Product.query.filter_by(name="First Product").first()
        product_2 = Product.query.filter_by(name="Second Product").first()

        assert "First Product" in product_1.name
        assert "Second Product" in product_2.name
        
    def test_products_is_saved(self):
        assert 2 == Product.query.count()


class TestForm(TestBase):
    def test_form_validation(self):
        pass
