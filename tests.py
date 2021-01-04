import pytest
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client


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