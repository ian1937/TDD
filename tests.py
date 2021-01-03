import unittest
import app


class TestHomeRoute(unittest.TestCase):

    def setUp(self):
        app.app.config['TESTING'] = True
        self.app = app.app.test_client()

    def test_page_displays_html(self):
        response = self.app.get('/')
        content = response.data
        self.assertIn(b'</html>', content)


if __name__ == '__main__':
    unittest.main()