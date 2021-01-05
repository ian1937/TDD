import pytest
from app import app, db
from models import Item


@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    app.app_context().push()

    with app.test_client() as client:
        yield client

    db.session.remove()
    db.drop_all()


class TestHomeRoute:
    def response_data(self, client):
        response = client.get('/')
        content = response.data
        return content

    @pytest.mark.parametrize("attribute", [
        b"html",
        b"head",
        b"css",
        b"body",
        b"form",
        b"input",
        b"submit",
    ])

    def test_has_attribute(self, client, attribute):
        assert (attribute) in self.response_data(client)
    
    def test_takes_POST_request(self, client):
        response = client.post('/', data={'input': 'Say Hello'})
        assert b"Say Hello" in self.response_data(client)

    def test_renders_data(self):
        pass


class TestDatabaseModel:

    def test_database_is_working(self):
        item1 = Item(text="First Item")
        item2 = Item(text="Second Item")

        db.session.add(item1)
        db.session.add(item2)

        db.session.commit()

        assert "First Item" in Item.objects.all()[0]
        assert "Second Item" in Item.objects.all()[1]
