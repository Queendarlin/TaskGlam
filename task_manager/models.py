from task_manager import db, login_manager, bcrypt
from flask_login import UserMixin
from datetime import datetime

"""
Script to define the models for the flask application
"""


@login_manager.user_loader
def load_user(user_id):
    """
        Load a user given their user ID.

        Args:
            user_id (int): The ID of the user.

        Returns:
            User: The user object with the specified user ID.
        """
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    """
        User model representing a user in the database.

        Attributes:
            id (int): The primary key for the user.
            username (str): The username of the user.
            email_address (str): The email address of the user.
            password_hash (str): The hashed password of the user.
            tasks (list): List of tasks associated with the user.
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    email_address = db.Column(db.String(50), nullable=False, unique=True)
    password_hash = db.Column(db.String(60), nullable=False)
    tasks = db.relationship('Task', backref='owner', lazy=True)

    @property
    def password(self):
        """
            Dummy password property to handle password hashing.

            Returns:
                str: The password hash.
        """
        return self.password

    @password.setter
    def password(self, plain_text_password):
        """
            Hash the plain text password
            and store it in the password_hash attribute.

            Args:
                plain_text_password (str): The plain text password.
        """
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password_correction(self, attempted_password):
        """
            Check if the provided password matches the stored password hash.

            Args:
                attempted_password (str): The password to check.

            Returns:
                bool: True if the password matches, False otherwise.
        """
        return bcrypt.check_password_hash(self.password_hash, attempted_password)


class Task(db.Model):
    """
        Task model representing a task in the database.

        Attributes:
            id (int): The primary key for the task.
            title (str): The title of the task.
            description (str): The description of the task.
            priority (str): The priority of the task.
            created_at (datetime): The timestamp when the task was created.
            updated_at (datetime): The timestamp when the task was last updated.
            due_date (datetime): The due date of the task.
            completed (bool): The completion status of the task.
            user_id (int): The ID of the user who owns the task.
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    priority = db.Column(db.String(50), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)
    due_date = db.Column(db.DateTime, nullable=True)
    completed = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        """
            Return a string representation of the task.
            Returns:
                str: String representation of the task.
        """
        return f"Task('{self.title}', '{self.description}')"
