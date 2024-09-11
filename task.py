from datetime import datetime
import re

class Task:

    def __init__(self, task_task_id, title, description, priority, due_date, status, assigned_user=None, category=None):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.status = status
        self.assigned_user = assigned_user
        self.category = category

    # Methods
    def update_title(self, title):
        self.title = title

    def update_description(self, description):
        self.description = description

    def update_priority(self, priority):
        self.priority = priority

    def update_due_date(self, due_date):
        self.due_date = due_date

    def update_status(self, status):
        self.status = status

    def assign_user(self, user):
        self.assigned_user = user

    def add_category(self, category):
        if self.category is None:
            self.category = []
        if category not in self.category:
            self.category.append(category)

    def remove_category(self, category):
        if category is not None and category in self.category:
            self.category.remove(category)

    def get_task_info(self):
        task_info = {
            "task_id": self.task_id,
            "title": self.title,
            "description": self.description,
            "priority": self.priority,
            "due_date": self.due_date,
            "status": self.status,
            "assigned_user": self.assigned_user,
            "category": self.category
        }

        return task_info

class User:

    def __init__(self, task_id, name, email, role, tasks):
        self.task_id = task_id
        self.name = name
        self.email = email
        self.role = role
        self.tasks = []

    # Methods
    def update_name(self, name):
        self.name = name

    def update_email(self, email):
        if re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email) is not None:
            self.email = email
        else:
            print("Please enter a valid email!")

    def update_role(self, role):
        self.role = role

    def assign_task(self, task):
        if task not in self.tasks:
            self.tasks.append(task)

    def remove_task(self, task):
        if self.tasks is not None and task in self.tasks:
            self.tasks.remove(task)

    def get_user_info(self):
        return {
            "task_id": self.task_id,
            "name": self.name,
            "email": self.email,
            "role": self.role,
            "tasks": self.tasks
        }

    def get_assigned_tasks(self):
        if self.tasks is not None:
            return self.tasks

class Category:

    def __init__(self, name, tasks):
        self.name = name
        self.tasks = []

    # Methods
    def add_task(self, task):
        if task not in self.tasks:
            self.tasks.append(task)

    def remove_task(self, task):
        if self.tasks is not None and task in self.tasks:
            self.tasks.remove(task)

    def get_category_info(self, task):
        return {
            "category name": self.name,
            "tasks": [task.get_task_info for task in self.tasks]
        }


class TaskManager:
    def __init__(self):
        self.categories = []  # List of Category objects
        self.tasks = []  # List of Task objects
        self.users = []  # List of User objects

    def add_category(self, category):
        """Add a new category to the manager."""
        if category not in self.categories:
            self.categories.append(category)

    def remove_category(self, category):
        """Remove a category from the manager."""
        if category in self.categories:
            self.categories.remove(category)

    def add_task(self, task):
        """Add a new task to the manager."""
        if task not in self.tasks:
            self.tasks.append(task)

    def remove_task(self, task):
        """Remove a task from the manager."""
        if task in self.tasks:
            self.tasks.remove(task)

    def add_user(self, user):
        """Add a new user to the manager."""
        if user not in self.users:
            self.users.append(user)

    def remove_user(self, user):
        """Remove a user from the manager."""
        if user in self.users:
            self.users.remove(user)

    def get_category_info(self, category_name):
        """Retrieve information about a category by its name."""
        category = next((cat for cat in self.categories if cat.name == category_name), None)
        if category:
            return {
                'name': category.name,
                'task_names': [task.title for task in category.tasks]
            }
        return None

    def assign_task(self, task_id, user_id):
        """Assign a task to a user by task_id."""
        # Find the task with the given task_id
        task = next((t for t in self.tasks if t.task_id == task_id), None)

        # Find the user with the given user_id
        user = next((u for u in self.users if u.user_id == user_id), None)

        if task and user:
            task.assigned_user = user

    def get_task(self, task_id):
        """Retrieve a task by its ID."""
        return next((task for task in self.tasks if task.task_id == task_id), None)

    def get_user_tasks(self, user_id):
        """Retrieve tasks assigned to a specific user by user_id."""
        return [task for task in self.tasks if task.assigned_user and task.assigned_user.user_id == user_id]

class Notification:
    def __init__(self, message, recipient, timestamp=None):
        """Initializes a new notification with the provided message, recipient, and timestamp."""
        self.message = message
        self.recipient = recipient  # Expecting a User object
        self.timestamp = timestamp if timestamp else datetime.now()

    def send(self):
        """Sends the notification to the recipient."""
        # Logic to send the notification, e.g., email or UI display
        # For demonstration purposes, we'll just print the notification
        print(f"Sending notification to {self.recipient.name}: {self.message} (Sent at: {self.timestamp})")

    def get_notification_info(self):
        """Retrieves the details of the notification."""
        return {
            'message': self.message,
            'recipient': self.recipient.name,
            'timestamp': self.timestamp.strftime('%Y-%m-%d %H:%M:%S')
        }