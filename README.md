##Todo App

## Python Package Dependencies
1. Django
2. smtp
3. apscheduler
4. psycopg2

## Quick start running the project
 1. clone repo `https://github.com/asif001/todoapp.git`
 2. Install required python dependencies into your python virtual environment (python-3.7.5) - `pip install -r requirements.txt`
 3. Setup postgres database and create database named 'todoapp'
 4. Give user and password in Databases in settings.py
 5. create superuser following https://docs.djangoproject.com/en/1.8/intro/tutorial02/
 6. Go to address http://127.0.0.1:8000/admin and add categories
 8. migrate database using `python manage.py makemigrations` and `python manage.py migrate`
 9. After successful migration execute `python manage.py runserver`
 10. Go to address http://127.0.0.1:8000/Todo
11. enjoy


## Introduction
In this project,I designed an django based app for todo list.Here anyone can add task, delete task, update task.Again for email notification he/she can give email address.When the schedule will come he/she will be notified

## Features
* Add task
* Delete task
* Update task
* Mail system at the time of schedule

## Contributing
The main reason to publish something open source, is that anyone can just jump in and start contributing to my project.
So If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcome.


## Author
Asifur Rahman
asifurarahman@gmail.com
Student at Department of Computer Science and Engineering
Khulna University of Engineering & Technology, Khulna
Bangladesh
