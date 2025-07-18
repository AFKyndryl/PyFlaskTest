import unittest
from app import app

class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page_pass(self):
        """Should PASS: 'Spaghetti Carbonara' is on the menu."""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Spaghetti Carbonara', response.data.decode())

    def test_home_page_fail(self):
        """Should FAIL: 'Pizza Margherita' is NOT on the menu."""
        response = self.app.get('/')
        self.assertIn('Pizza Margherita', response.data.decode())

    def test_invalid_route_pass(self):
        """Should PASS: /nonexistent should return 404."""
        response = self.app.get('/nonexistent')
        self.assertEqual(response.status_code, 404)

    def test_invalid_status_code_fail(self):
        """Should FAIL: expecting 200 from a 404 route."""
        response = self.app.get('/nonexistent')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(FlaskAppTestCase)
    result = unittest.TextTestRunner(verbosity=2).run(suite)

    if result.wasSuccessful():
        print("\n✅ ALL TESTS PASSED")
    else:
        print("\n❌ SOME TESTS FAILED")
