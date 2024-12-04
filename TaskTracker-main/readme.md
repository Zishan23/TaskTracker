# TaskTracker
Get ready to boost your productivity and stay on top of your to-do list. TaskTracker simplifies task management, helping you focus on what matters most. Sign in now to get started! TaskTracker allows users to sign up, sign in, add and delete tasks, and log out.


## Features
User registration and login
Task creation and deletion
User authentication (sign in, sign out)
User-specific task management

# ScreenShots
![image](https://github.com/allengarcia04/TaskTracker/assets/154303616/6e3d069a-51f0-4ab0-afc9-e1ba5b28cf7b)
![image](https://github.com/allengarcia04/TaskTracker/assets/154303616/48633d5a-5e17-4622-a6c0-77381454dea1)

# Technologies Used
- **Backend**: Python, Flask, SQLAlchemy
- **Frontend**: HTML, CSS, JavaScript
- **Other**: Flask-Login for authentication, SQLite for the database

# Installation and Setup
Prerequisites
Python 3.11 or later
Pip (Python package installer)
Virtual environment tool (optional but recommended)
Installation Steps
1. Clone the repository
2. Navigate to the project directory:
`cd TaskTracker`
4. Create and activate a virtual environment (optional but recommended):
`python -m venv venv`
`source venv/bin/activate`  # On Windows use `venv\Scripts\activate`
5. Install dependencies:
`pip install -r requirements.txt`
7. Set up the database:
Ensure the DB_NAME in website/__init__.py is set to database.db. Then, run the following commands to create the database: flask shell
`from website import db
db.create_all()
exit()`
8. Run the flask server:
`flask run`
10. Open your web browser and navigate to http://127.0.0.1:5000.

## Usage
1. Sign Up: Register a new account.
2. Sign In: Log in to your account.
3. Add Tasks: Create new tasks to manage.
4. Delete Tasks: Remove tasks that are no longer needed.
5. Log Out: Sign out of your account when done.




















