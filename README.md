## Python Package Dependencies
1. django
2. smtp
3. apscheduler
4. psycopg2

## Quick start running the project
 1. clone repo `https://github.com/asif001/todoapp.git`
 2. Install required python dependencies into your python virtual environment.
 3. Setup postgres database and create database named 'todoapp'
 4. Give user and password in Databases in settings.py
 5. create superuser following https://docs.djangoproject.com/en/1.8/intro/tutorial02/
 6. Go to address http://127.0.0.1:8000/admin and add categories
 7. migrate database using 'python manage.php migrate'
 8. After successful migration execute `python manage.py runserver`
 9. Go to address http://127.0.0.1:8000/Todo
10. enjoy
11. For any information kindly mail me at 'rahman1507001@stud.kuet.ac.bd'

## Introduction
In this project,I designed an django based app for todo list.Here anyone can add task, delete task, update task.Again for email notification he/she can give email address.When the schedule will come he/she will be notified

## Features
* Add task
* Delete task
* Update task
* Mail system at the time of schedule
