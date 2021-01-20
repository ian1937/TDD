import os
import pytest
import tempfile
from app import app, db
from app.models import Product


class TestBase:
    @pytest.fixture(scope='session', autouse=True)
    def client(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        app.app_context().push()

        with app.test_client() as client:
            db.create_all()
            yield client

        db.drop_all()

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
        response = client.post('/', data={'input': 'Say Hello'})
        assert b"Say Hello" in self.response_data(client)


class TestDatabase(TestBase):
    def test_database_is_working(self):
        product1 = Product(text="First Product")
        product2 = Product(text="Second Product")

        db.session.add(product1)
        db.session.add(product2)

        db.session.commit()

        product_1 = Product.query.filter_by(text="First Product").first()
        product_2 = Product.query.filter_by(text="Second Product").first()

        assert "First Product" in product_1.text
        assert "Second Product" in product_2.text
        
    def test_products_is_saved(self):
        assert 3 == Product.query.count()

    def test_data_is_rendered(self, client):
        assert b"First Product" in self.response_data(client)
        assert b"Second Product" in self.response_data(client)
