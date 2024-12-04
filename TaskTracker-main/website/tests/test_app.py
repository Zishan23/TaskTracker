import unittest
from website import create_app, db  # Import your Flask app factory and db instance
from website.models import User, Note  # Import your models
from flask import url_for

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        # Create a test app instance
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # In-memory database
        self.app.config['WTF_CSRF_ENABLED'] = False  # Disable CSRF for testing

        # Create a test client
        self.client = self.app.test_client()

        # Set up the database
        with self.app.app_context():
            db.create_all()

            # Add a test user
            test_user = User(email='test@example.com', first_name='Test', password='password')
            db.session.add(test_user)
            db.session.commit()

    def tearDown(self):
        # Drop the database after every test
        with self.app.app_context():
            db.drop_all()

    def test_login(self):
        # Send a POST request to the login route
        response = self.client.post('/login', data={
            'email': 'test@example.com',
            'password': 'password'
        }, follow_redirects=True)

        # Check if login was successful
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hi Test!', response.data)  

    def test_task_post(self):
        # Log in first
        self.client.post('/login', data={
            'email': 'test@example.com',
            'password': 'password'
        }, follow_redirects=True)

        # Post a new task
        response = self.client.post('/', data={
            'note': 'Test Task',
        }, follow_redirects=True)

        # Check if task was added
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test Task', response.data)  # Look for the task text in the response

        # Ensure the task exists in the database
        with self.app.app_context():
            note = Note.query.filter_by(data='Test Task').first()
            self.assertIsNotNone(note)


if __name__ == '__main__':
    unittest.main()


