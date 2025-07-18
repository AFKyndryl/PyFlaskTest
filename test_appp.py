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

    def test_home_page_contains_menu(self):
        """Should PASS: Menu contains at least one known item."""
        response = self.app.get('/')
        self.assertTrue(any(dish in response.data.decode() for dish in [
            'Spaghetti Carbonara', 'Penne Arrabbiata', 'Fettuccine Alfredo'
        ]))

    def test_invalid_route_returns_404(self):
        """Should PASS: /nonexistent should return 404."""
        response = self.app.get('/nonexistent')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(FlaskAppTestCase)
    result = unittest.TextTestRunner(verbosity=2).run(suite)

    if result.wasSuccessful():
        print("\n✅ ALL TESTS PASSED")
    else:
        print("\n❌ SOME TESTS FAILED")

