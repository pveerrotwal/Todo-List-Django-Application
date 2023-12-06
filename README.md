## Technology Stack used:

Backend:
1. Python 3.11+
2. Django 4.2.7+
3. Django Rest Framework 3.14.0+
Test your codebase:
1. Postman Collection

## Setup Instructions


1. Navigate into the project directory (`source_code/`).
2. Create a virtual environment in a `venv/` folder by typing `python -m venv venv` in your console.
3. Activate the venv using `source venv/bin/activate` (Linux, MacOS) or `venv\Scripts\activate.bat` (Windows).
4. Install the dependencies with `python -m pip install -r requirements.txt`
5. Generate the empty SQLite database and tables using `python manage.py migrate`
5. Run the app with `python manage.py runserver`
6. Browse to the [app home page](http://localhost:8000/) to see the list of todo lists, which will initially be empty. 

You can now start using the UI to add your to-do lists and to-do items to the database. The data will be stored in a new `db.sqlite3` file in the root of your project directory.

You can also use Django's auto-generated [admin interface](https://realpython.com/customize-django-admin-python/#setting-up-the-django-admin) at `http://localhost:8000/admin/` to view, add, and edit the data.

## Working
Description: Designed the backend for a web-based To-do List application, as per the given requirements:
1. Created a Django app with appropriate models to store information for the To-do List app. The app should be able to store the following information:

<img width="578" alt="Screenshot 2023-12-04 at 6 42 31 PM" src="https://github.com/pveerrotwal/Todo-List-Django-Application/assets/108364147/e4c17eec-1000-4d72-a471-060dd5753f03">

a. Timestamp: Timestamp at which a task was created.
Should be auto-set when creating a new entry. A user should not be able to edit this.
b. Title: Title of the task to be done.
i. A user can set this while creating a new entry. A user can also change
this while updating an existing entry.
ii. Max length: 100 characters.
iii. Mandatory field
<img width="652" alt="Screenshot 2023-12-04 at 6 42 23 PM" src="https://github.com/pveerrotwal/Todo-List-Django-Application/assets/108364147/d96b7be0-62ea-4374-958c-41dbb4b45e49">

c. Description: Description of the task to be done.
i. A user can add details about this task.
ii. Max length: 1000 characters
iii. Mandatory field
d. Due Date: Expected due date to finish the task
i. A user can set this while creating a new entry. A user can also change this while updating an existing entry.
ii. Optional field
e. Tag: One or more tags that the user can add to the entry
i. A user can set this while creating a new entry. A user can also change this while updating an existing entry. Multiple tags can be added to the same entry
ii. Optional field
iii. Multiple tags with the same value should be saved only once.
f. Status: Shows the status of a task
Should be one of these values.
1. OPEN (Default value)
2. WORKING
3. DONE
4. OVERDUE



6. The following REST APIs created using DRF (DjangoRestFramework). Use class-based views:
a. CREATE a todo item
b. READ one todo item
c. READ all todo items
d. UPDATE a todo item
e. DELETE a todo item

## Django Administration
<img width="1411" alt="Screenshot 2023-12-04 at 10 33 39 PM" src="https://github.com/pveerrotwal/Todo-List-Django-Application/assets/108364147/23f2fca4-192a-4a0a-bf77-6001fb672d61">


## CI/CD
Implemented the below-mentioned GitHub actions for my GitHub repo:
1. Run tests automatically:
a. Unit tests
b. Integration tests
2. Run linting tools:
a. Flake8 b. Black

## Coverage Report:

<img width="523" alt="Screenshot 2023-12-06 at 12 58 28 PM" src="https://github.com/pveerrotwal/Todo-List-Django-Application/assets/108364147/21415f3c-b43f-486f-b310-b0e77a07ddb9">

## GitHub Repository:
"https://github.com/pveerrotwal/Todo-List-Django-Application"
