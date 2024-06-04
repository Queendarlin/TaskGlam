from task_manager import app, db
from flask import render_template, redirect, url_for, flash, jsonify, request
from task_manager.models import User, Task
from task_manager.forms import RegisterForm, LoginForm, AddTaskForm
from flask_login import login_user, logout_user, login_required, current_user

"""
This Flask application manages user tasks with features like registration,
login, account settings, adding, editing, deleting, marking tasks as complete,
and retrieving tasks through an API endpoint.
"""


@app.route('/')
@app.route('/home')
def home_page():
    """
    Render the home page. Redirect authenticated users to the tasks page.
    """
    if current_user.is_authenticated:
        return redirect(url_for('tasks_page'))
    return render_template('home.html')


@app.route('/register', methods=['GET', 'POST'])
def register_page():
    """
    Handle user registration. Create a new user if the form is valid,
    log them in, and redirect to the add task page.
    """
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email_address=form.email_address.data,
                              password=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        flash(f"Account successfully created! You are logged in as: {user_to_create.username}", category='success')
        return redirect(url_for('tasks_page'))
    if form.errors != {}:  # If there are errors from the validations
        for err_msg in form.errors.values():
            flash(f'There was an error creating a user: {err_msg}',
                  category='danger')

    return render_template('register.html', form=form)


@app.route('/account_settings', methods=['GET', 'POST'])
@login_required
def account_settings():
    """
    Render and handle updates to the user's account settings. Update email,
    username, and password if provided.
    """
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        current_password = request.form.get('current_password')
        new_password = request.form.get('new_password')
        confirm_new_password = request.form.get('confirm_new_password')

        # Check if the current password is correct
        if not current_user.check_password_correction(current_password):
            flash('Current password is incorrect', 'danger')
            return redirect(url_for('account_settings'))

        # Update email and username
        if email:
            current_user.email_address = email

        if username:
            current_user.username = username

        # Update password if new password is provided and confirmed
        if new_password and new_password == confirm_new_password:
            current_user.password = new_password

        db.session.commit()
        flash('Account updated successfully', 'success')
        return redirect(url_for('account_settings'))

    return render_template('account_settings.html')


@app.route('/update_account', methods=['POST'])
@login_required
def update_account():
    """
    Update the user's account details (email, username, and password)
    based on form input.
    """
    email = request.form.get('email')
    username = request.form.get('username')
    current_password = request.form.get('current_password')
    new_password = request.form.get('new_password')
    confirm_new_password = request.form.get('confirm_new_password')

    # Check if the current password is correct
    if not current_user.check_password_correction(current_password):
        flash('Current password is incorrect', 'danger')
        return redirect(url_for('account_settings'))

    # Update email and username
    if email:
        current_user.email_address = email

    if username:
        current_user.username = username

    # Update password if new password is provided and confirmed
    if new_password and new_password == confirm_new_password:
        current_user.password = new_password

    db.session.commit()
    flash('Account updated successfully', 'success')
    return redirect(url_for('account_settings'))


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    """
    Handle user login. Authenticate and log in the user if the form is valid.
    """
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(
                attempted_password=form.password.data
        ):
            login_user(attempted_user)
            flash(f'Successfully logged in as: {attempted_user.username}', category='success')
            return redirect(url_for('tasks_page'))
        else:
            flash('The username and password do not match! Please try again', category='danger')

    return render_template('login.html', form=form)


@app.route('/logout')
def logout_page():
    """
    Log the user out and redirect to the home page.
    """
    logout_user()
    flash("You have successfully logged out!", category='info')
    return redirect(url_for('home_page'))


@app.route('/add_task', methods=['GET', 'POST'])
@login_required
def add_task():
    """
    Handle task creation. Add a new task if the form is valid and
    redirect to the tasks page.
    """
    form = AddTaskForm()
    if form.validate_on_submit():
        new_task = Task(
            title=form.title.data,
            description=form.description.data,
            priority=form.priority.data,
            due_date=form.due_date.data,
            completed=form.completed.data,
            user_id=current_user.id
        )
        db.session.add(new_task)
        db.session.commit()
        flash('Task added successfully!', category='success')
        return redirect(url_for('tasks_page'))
    return render_template('add_task.html', form=form)


@app.route('/tasks')
@login_required
def tasks_page():
    """
    Render the tasks page, displaying all tasks for the current user.
    """
    tasks = Task.query.filter_by(user_id=current_user.id).all()
    return render_template('tasks.html', tasks=tasks)


@app.route('/api/tasks', methods=['GET'])
@login_required
def get_tasks():
    """
    API endpoint to retrieve all tasks for the current user.
    """
    tasks = Task.query.filter_by(user_id=current_user.id).all()
    tasks_list = [
        {
            "id": task.id,
            "title": task.title,
            "description": task.description,
            "priority": task.priority,
            "created_at": task.created_at,
            "updated_at": task.updated_at,
            "due_date": task.due_date,
            "completed": task.completed
        }
        for task in tasks
    ]
    return jsonify(tasks_list)


@app.route('/tasks/<int:task_id>', methods=['DELETE'])
@login_required
def delete_task(task_id):
    """
    Handle task deletion.
    Delete the task with the given ID if it belongs to the current user.
    """
    task = Task.query.get(task_id)
    if task and task.user_id == current_user.id:
        db.session.delete(task)
        db.session.commit()
        return jsonify(success=True), 200
    return jsonify(success=False), 404


@app.route('/tasks/<int:task_id>/complete', methods=['POST'])
@login_required
def complete_task(task_id):
    """
    Mark a task as completed or not completed.
    Update the task's completion status based on the provided data.
    """
    task = Task.query.get(task_id)
    if task and task.user_id == current_user.id:
        data = request.get_json()
        task.completed = data['completed']
        db.session.commit()
        return jsonify(success=True), 200
    return jsonify(success=False), 404


@app.route('/tasks/<int:task_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_task(task_id):
    """
    Handle task editing.
    Update the task with the given ID if it belongs to the current user.
    """
    task = Task.query.get_or_404(task_id)
    if task.user_id != current_user.id:
        flash("You don't have permission to edit this task.", 'danger')
        return redirect(url_for('tasks_page'))

    form = AddTaskForm()
    if form.validate_on_submit():
        task.title = form.title.data
        task.description = form.description.data
        task.priority = form.priority.data
        task.due_date = form.due_date.data
        db.session.commit()
        flash('Task updated successfully!', 'success')
        return redirect(url_for('tasks_page'))

    elif request.method == 'GET':
        form.title.data = task.title
        form.description.data = task.description
        form.priority.data = task.priority
        form.due_date.data = task.due_date

    return render_template('edit_task.html', form=form, task_id=task.id)
