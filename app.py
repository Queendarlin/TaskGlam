from task_manager import app, db

"""
This script serves as the entry point for running the Flask development server
and creating the database tables (if they don't already exist).

It's typically executed directly and not imported as a module.
"""

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
