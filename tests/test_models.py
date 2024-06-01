import unittest
from task_manager.models import User, Task
from task_manager import db


class TestTaskModel(unittest.TestCase):
    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

# ... Test cases for User and Task models ...
    def test_create_user(self):
        user = User(username="test_user", email_address="test@example.com", password="password123")
        db.session.add(user)
        db.session.commit()

        fetched_user = User.query.get(user.id)
        self.assertEqual(fetched_user.username, "test_user")
        self.assertEqual(fetched_user.email_address, "test@example.com")
        # Password hash is verified indirectly through check_password_correction test

    def test_unique_username_email(self):
        # Test uniqueness of username and email
        user1 = User(username="test_user", email_address="test@example.com", password="password123")
        db.session.add(user1)
        db.session.commit()

        with self.assertRaises(ValueError):
            user2 = User(username="test_user", email_address="different@example.com", password="password456")
            db.session.add(user2)
            db.session.commit()  # Should raise an error for duplicate username

        with self.assertRaises(ValueError):
            user3 = User(username="unique_username", email_address="test@example.com", password="password789")
            db.session.add(user3)
            db.session.commit()  # Should raise an error for duplicate email

    def test_user_password_hashing(self):
        user = User(username="test_user", email_address="test@example.com", password="password123")
        self.assertNotEqual(user.password_hash, "password123")  # Password should be hashed
        self.assertTrue(bcrypt.check_password_hash(user.password_hash, "password123"))

    def test_check_password_correction(self):
        user = User(username="test_user", email_address="test@example.com", password="password123")
        db.session.add(user)
        db.session.commit()

        fetched_user = User.query.get(user.id)
        self.assertTrue(fetched_user.check_password_correction("password123"))
        self.assertFalse(fetched_user.check_password_correction("wrong_password"))

    def test_create_task(self):
        user = User(username="test_user", email_address="test@example.com", password="password123")
        db.session.add(user)
        db.session.commit()

        task = Task(title="Write unit tests", description="Test TaskGlam models", owner=user)
        db.session.add(task)
        db.session.commit()

        fetched_task = Task.query.get(task.id)
        self.assertEqual(fetched_task.title, "Write unit tests")
        self.assertEqual(fetched_task.description, "Test TaskGlam models")
        self.assertEqual(fetched_task.owner, user)  # Verify owner relationship

    def test_task_validation(self):
        # Test validation for required fields (title)
        with self.assertRaises(ValueError):
            Task(description="Test description")  # Missing title raises an error
